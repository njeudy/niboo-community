
from openerp import tools, models, fields
from openerp.addons.decimal_precision import decimal_precision as dp


class hr_timesheet_report(models.Model):
    _name = "account.analytic.report"
    _description = "Analytic"
    _auto = False

    date = fields.Date('Date', readonly=True)
    name = fields.Char('Description', group_operator='max')
    line = fields.Char('Line', readonly=True, group_operator='max')
    analytic_account_id = fields.Many2one('account.analytic.account', 'Analytic Account', readonly=True)
    company_id = fields.Many2one('res.company', 'Company', readonly=True)
    move_name = fields.Char('Move', group_operator='max')
    product = fields.Char('Product', group_operator='max')
    general_account = fields.Char('General Account', group_operator='max')
    quantity = fields.Float('Quantity')
    amount = fields.Float('Amount')
    axis_id = fields.Many2one('account.analytic.axis', 'Axis', readonly=True)

    def _select(self):
        select_str = """
SELECT
min(aal.id) as id,
to_char(aal.id, '9999999999999999999999') as line,
aal.date,
aal.name,
aal.account_id as analytic_account_id,
pp.name_template as product,
aal.company_id,
aa.code as general_account,
COALESCE(am.name, ' ') as move_name,
sum(aal.unit_amount) as quantity,
sum(aal.amount) as amount,
aaa.analytic_account_axis_id as axis_id
"""
        return select_str

    def _from(self):
        from_str = """
            FROM account_analytic_line aal
            LEFT JOIN account_move am ON aal.move_id = am.id
            LEFT JOIN product_product pp ON aal.product_id = pp.id,
            account_analytic_account aaa, account_account aa

        """
        return from_str

    def _group_by(self):
        group_by_str = """
            GROUP BY aal.date,
                    aal.account_id,
                    aaa.analytic_account_axis_id,
                    am.name,
                    aal.company_id,
                    aal.currency_id,
                    aal.ref,
                    aal.name,
                    pp.name_template,
                    aa.code,
                    line
        """
        return group_by_str

    def _where(self):
        where_str = """
            WHERE aal.account_id = aaa.id
            AND aa.id = aal.general_account_id
        """
        return where_str

    def init(self, cr):
        # self._table = hr_timesheet_report
        tools.drop_view_if_exists(cr, self._table)
        cr.execute("""CREATE or REPLACE VIEW %s as (
            %s
            %s
            %s
            %s
            )""" % (self._table, self._select(), self._from(), self._where(), self._group_by()))

    def read_group(self, cr, uid, domain, fields, groupby, offset=0, limit=None, context=None, orderby=False, lazy=True):
        """
        Get the list of records in list view grouped by the given ``groupby`` fields

        :param cr: database cursor
        :param uid: current user id
        :param domain: list specifying search criteria [['field_name', 'operator', 'value'], ...]
        :param list fields: list of fields present in the list view specified on the object
        :param list groupby: list of groupby descriptions by which the records will be grouped.
                A groupby description is either a field (then it will be grouped by that field)
                or a string 'field:groupby_function'.  Right now, the only functions supported
                are 'day', 'week', 'month', 'quarter' or 'year', and they only make sense for
                date/datetime fields.
        :param int offset: optional number of records to skip
        :param int limit: optional max number of records to return
        :param dict context: context arguments, like lang, time zone.
        :param list orderby: optional ``order by`` specification, for
                             overriding the natural sort ordering of the
                             groups, see also :py:meth:`~osv.osv.osv.search`
                             (supported only for many2one fields currently)
        :param bool lazy: if true, the results are only grouped by the first groupby and the
                remaining groupbys are put in the __context key.  If false, all the groupbys are
                done in one call.
        :return: list of dictionaries(one dictionary for each record) containing:

                    * the values of fields grouped by the fields in ``groupby`` argument
                    * __domain: list of tuples specifying the search criteria
                    * __context: dictionary with argument like ``groupby``
        :rtype: [{'field_name_1': value, ...]
        :raise AccessError: * if user has no read rights on the requested object
                            * if user tries to bypass access rules for read on the requested object
        """
        if context is None:
            context = {}
        self.check_access_rights(cr, uid, 'read')
        query = self._where_calc(cr, uid, domain, context=context)
        fields = fields or self._columns.keys()

        groupby = [groupby] if isinstance(groupby, basestring) else groupby
        groupby_list = groupby[:1] if lazy else groupby
        annotated_groupbys = [
            self._read_group_process_groupby(cr, uid, gb, query, context=context)
            for gb in groupby_list
        ]
        groupby_fields = [g['field'] for g in annotated_groupbys]
        order = orderby or ','.join([g for g in groupby_list])
        groupby_dict = {gb['groupby']: gb for gb in annotated_groupbys}

        self._apply_ir_rules(cr, uid, query, 'read', context=context)
        for gb in groupby_fields:
            assert gb in fields, "Fields in 'groupby' must appear in the list of fields to read (perhaps it's missing in the list view?)"
            groupby_def = self._columns.get(gb) or (self._inherit_fields.get(gb) and self._inherit_fields.get(gb)[2])
            assert groupby_def and groupby_def._classic_write, "Fields in 'groupby' must be regular database-persisted fields (no function or related fields), or function fields with store=True"
            if not (gb in self._fields):
                # Don't allow arbitrary values, as this would be a SQL injection vector!
                raise UserError(_('Invalid group_by specification: "%s".\nA group_by specification must be a list of valid fields.') % (gb,))

        aggregated_fields = [
            f for f in fields
            if f not in ('id', 'sequence')
            if f not in groupby_fields
            if f in self._fields
            if self._fields[f].type in ('integer', 'float', 'monetary', 'char')
            if getattr(self._fields[f].base_field.column, '_classic_write', False)
        ]

        field_formatter = lambda f: (
            self._fields[f].group_operator or 'sum',
            self._inherits_join_calc(cr, uid, self._table, f, query, context=context),
            f,
        )
        select_terms = ["%s(%s) AS %s" % field_formatter(f) for f in aggregated_fields]

        for gb in annotated_groupbys:
            select_terms.append('%s as "%s" ' % (gb['qualified_field'], gb['groupby']))

        groupby_terms, orderby_terms = self._read_group_prepare(cr, uid, order, aggregated_fields, annotated_groupbys, query, context=context)
        from_clause, where_clause, where_clause_params = query.get_sql()
        if lazy and (len(groupby_fields) >= 2 or not context.get('group_by_no_leaf')):
            count_field = groupby_fields[0] if len(groupby_fields) >= 1 else '_'
        else:
            count_field = '_'
        count_field += '_count'

        prefix_terms = lambda prefix, terms: (prefix + " " + ",".join(terms)) if terms else ''
        prefix_term = lambda prefix, term: ('%s %s' % (prefix, term)) if term else ''

        query = """
            SELECT min(%(table)s.id) AS id, count(%(table)s.id) AS %(count_field)s %(extra_fields)s
            FROM %(from)s
            %(where)s
            %(groupby)s
            %(orderby)s
            %(limit)s
            %(offset)s
        """ % {
            'table': self._table,
            'count_field': count_field,
            'extra_fields': prefix_terms(',', select_terms),
            'from': from_clause,
            'where': prefix_term('WHERE', where_clause),
            'groupby': prefix_terms('GROUP BY', groupby_terms),
            'orderby': prefix_terms('ORDER BY', orderby_terms),
            'limit': prefix_term('LIMIT', int(limit) if limit else None),
            'offset': prefix_term('OFFSET', int(offset) if limit else None),
        }

        cr.execute(query, where_clause_params)
        fetched_data = cr.dictfetchall()

        if not groupby_fields:
            return fetched_data

        many2onefields = [gb['field'] for gb in annotated_groupbys if gb['type'] == 'many2one']
        if many2onefields:
            data_ids = [r['id'] for r in fetched_data]
            many2onefields = list(set(many2onefields))
            data_dict = {d['id']: d for d in self.read(cr, uid, data_ids, many2onefields, context=context)}
            for d in fetched_data:
                d.update(data_dict[d['id']])

        data = map(lambda r: {k: self._read_group_prepare_data(k,v, groupby_dict, context) for k,v in r.iteritems()}, fetched_data)
        result = [self._read_group_format_result(d, annotated_groupbys, groupby, groupby_dict, domain, context) for d in data]
        if lazy and groupby_fields[0] in self._group_by_full:
            # Right now, read_group only fill results in lazy mode (by default).
            # If you need to have the empty groups in 'eager' mode, then the
            # method _read_group_fill_results need to be completely reimplemented
            # in a sane way
            result = self._read_group_fill_results(cr, uid, domain, groupby_fields[0], groupby[len(annotated_groupbys):],
                                                       aggregated_fields, count_field, result, read_group_order=order,
                                                       context=context)


        if 'line' not in groupby and 'name' in fields:
            if 'name' in fields:
                for element in result:
                    element['name'] = ' '
            if 'move_name' in fields:
                for element in result:
                    element['move_name'] = ' '
        return result
