from flectra import api, models, fields,exceptions

class StudentData(models.Model):
    _name = 'student.data'

    def total_total_subject(self):
        for i in self:
            i.total_subject = len(i.subject_data_ids)

    state = fields.Selection([('draft','Draft'),
                              ('fillup','Fill Up'),
                              ('pending','Pending'),
                              ('done','Done')],default='draft')

    name = fields.Char(string="Name:")
    student_enrollno = fields.Char(string="Enroll No",required=True)
    student_sem = fields.Integer(string="Semester", size=1)
    student_stream = fields.Char(string="Stream",required=True)
    student_birthdate = fields.Date(string="Birth Date")
    student_fee = fields.Integer(string="Fee Of One Subject")
    final_price = fields.Integer()
    total_subject = fields.Integer(string="Total Subject")
    college_info_id = fields.Many2one('college.data', string="College Info")
    subject_data_ids = fields.Many2many('subject.data', string="Subject Data")

    @api.one
    def draft_statusbar(self):
        self.write({'state':'draft'})

    @api.one
    def fillup_statusbar(self):
        self.write({'state':'fillup'})

    @api.one
    def pending_statusbar(self):
        self.write({'state':'pending'})

    @api.one
    def done_statusbar(self):
        self.write({'state':'done'})

    @api.onchange("college_info_id","subject_data_ids")
    def _onchange_college_info_id_(self):
        self.student_fee = self.college_info_id.college_fee
        self.final_price = self.student_fee * len(self.subject_data_ids)

    @api.constrains('student_sem')
    def _check_sem_(self):
        if (self.student_sem > 8) or (self.student_sem <= 0 ):
            raise exceptions.ValidationError('Semester Value Is Incorrect ')

    _sql_constraints = [('enroll_uniq','UNIQUE(student_enrollno)','Enrollment Already Exists')]