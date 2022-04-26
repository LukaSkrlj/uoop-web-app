from django import template

register = template.Library()


@register.filter(name="getCourseDate")
def getCourseDate(value, arg): #arg is 'start' or 'end'
    return str(value[0][arg+'Date']).split("-")[0] #returns startDate year or endDate year


@register.filter(name="getSchoolYear")
def getSchoolYear(value):
    return str(value.startDate).split("-")[0] + "/" + str(value.endDate).split("-")[0] #returns startDate year or endDate year