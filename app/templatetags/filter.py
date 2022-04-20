from django import template

register = template.Library()


@register.filter(name="getCourseDate")
def getCourseDate(value, arg): #arg je ili 'start' ili 'end'
    return str(value[0][arg+'Date']).split("-")[0] #returns startDate year or endDate year


@register.filter(name="getSchoolYear")
def getSchoolYear(value):
    #ne mozes koristit ovu gore funkciju i ne mozes value['startDate'] jer kaze da Object Is Not Subscriptable,, nesto zbog ovog .get() unutar views.py
    return str(value.startDate).split("-")[0] + "/" + str(value.endDate).split("-")[0]