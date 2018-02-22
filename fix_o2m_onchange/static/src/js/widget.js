openerp.fix_o2m_onchange = function(instance) {

    instance.web.form.One2ManyListView.include({
        changed_records: function () {}
    });

    instance.web.BufferedDataSet.include({
        create: function(data, options) {
            var res = this._super.apply(this, arguments);
            if(!_.isEmpty(this.o2m)){
                this.o2m.trigger('created_value');
            }
            return res;
        }
    });

    instance.web.FormView.include({
        register_field: function (field, name) {
            this._super.apply(this, arguments);
            field.on('created_value', this, function() {
                this.trigger('field_changed:' + name);
                field._dirty_flag = true;
                this.do_onchange(field);
                this.on_form_changed(true);
                this.do_notify_change();
            });
        }
    });

};