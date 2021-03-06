from piston.handler import BaseHandler
from piston.utils import rc
from college.models import College, Coach, CollegeYear, CollegeCoach

class CollegeHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = College
    fields = ('id', 'updated', 'name', 'slug', ('state', ('id', 'name')), ('collegeyear_set', ('year','record','conference_record', 'division', ('conference', ('abbrev','name')))))
    exclude = ('official_url','official_rss', 'drive_slug')
    
    def read(self, request, slug):
        try:
            return College.objects.get(slug=slug)
        except College.DoesNotExist:
            return rc.NOT_FOUND
        except College.MultipleObjectsReturned:
            return rc.BAD_REQUEST
        
    
    @classmethod
    def resource_uri(cls, college):
        return ('colleges', ['json',])

class CollegeYearHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = CollegeYear
    fields = ('year','record','conference_record', 'division', ('conference', ('abbrev','name')))
    exclude = ('id', 'official_url','official_rss', 'drive_slug')

    def read(self, request, slug, season):
        try:
            return CollegeYear.objects.select_related().get(college__slug=slug, season=season)
        except CollegeYear.DoesNotExist:
            return rc.NOT_FOUND
        except CollegeYear.MultipleObjectsReturned:
            return rc.BAD_REQUEST


    @classmethod
    def resource_uri(cls, college):
        return ('colleges', ['json',])
        
class CoachHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Coach
    fields = ('id', 'updated', 'name', 'slug', ('state', ('id', 'name')), ('collegeyear_set', ('year','record','conference_record', 'division', ('conference', ('abbrev','name')))))
    exclude = ('official_url','official_rss', 'drive_slug')

    def read(self, request, slug):
        try:
            return Coach.objects.get(slug=slug)
        except Coach.DoesNotExist:
            return rc.NOT_FOUND
        except Coach.MultipleObjectsReturned:
            return rc.BAD_REQUEST


    @classmethod
    def resource_uri(cls, coach):
        return ('coaches', ['json',])