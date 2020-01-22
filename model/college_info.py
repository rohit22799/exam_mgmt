from flectra import api,fields,models

class CollegeData(models.Model):
    _name = 'college.data'

    def total_total_student1(self):
        for i in self:
            i.total_student = len(i.college_info_line)

    name = fields.Char(string="Name")
    college_code = fields.Char(string="College Code")
    college_address = fields.Char(string="College Address")
    college_fee = fields.Integer(string="Fee Of One Subject")
    total_student = fields.Integer(string="Total student")
    college_info_line = fields.One2many('student.data', 'college_info_id', string="student Info")