from flectra import api, models, fields

class SubjectData(models.Model):
    _name = 'subject.data'

    name = fields.Char(string="Subject")