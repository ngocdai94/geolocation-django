from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import GeolocationData, GeolocationInformation

# Create your tests here.             
##----------------------------- TESTING MODELS ------------------------------##
class GeolocationInformationTest(TestCase):
   def test_string(self):
      type=GeolocationInformation(geodescription='Reverse Geolocation')
      self.assertEqual(str(type), type.geodescription)

   def test_table(self):
      self.assertEqual(str(GeolocationInformation._meta.db_table), 'geodescription')

class GeolocationDataTest(TestCase):  
   def setup(self):
      geodata=GeolocationData(
        geoname='Seattle',
        latdegree=47.47,
        latminute=28,
        latsecond=28.696,
        latdirection='N',
        longdegree=122,
        longminute=20,
        longsecond=19.136,
        longdirection='W',
        latitude=47.47,
        longitude=-122.33,
        altitude=105)
      return geodata

   def test_string(self):
      geodata=self.setup()
      self.assertEqual(str(geodata), geodata.geoname)

   def test_table(self):
      self.assertEqual(str(GeolocationData._meta.db_table), 'geolocationdata')
##---------------------------- TESTING MODELS ENDS --------------------------##

##----------------------------- TESTING VIEWS ------------------------------##
## Sample Data
class IndexTest(TestCase):
   def test_view_url_accessible_by_name(self):
      response = self.client.get(reverse('index'))
      self.assertEqual(response.status_code, 200)

class getGeolocationDataTest(TestCase):
   def test_view_url_accessible_by_name(self):
      response = self.client.get(reverse('geodata'))
      self.assertEqual(response.status_code, 200)
##----------------------------- TESTING VIEWS ENDS ------------------------------##

##----------------------------- AUTHENTICATION TESTS ------------------------------##
class New_GeoData_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.resource=GeolocationData.objects.create(geoname='Seattle',
                                                    latdegree=47.47,
                                                    latminute=28,
                                                    latsecond=28.696,
                                                    latdirection='N',
                                                    longdegree=122,
                                                    longminute=20,
                                                    longsecond=19.136,
                                                    longdirection='W',
                                                    latitude=47.47,
                                                    longitude=-122.33,
                                                    altitude=105)

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newgeodata'))#newgeodata is the name "name" in urls.py
        self.assertRedirects(response, '/accounts/login/?next=/geolocationapp/newGeolocationData/')#method in views.py

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newgeodata'))#newgeodata is the name "name" in urls.py
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'geolocationapp/newgeodata.html')
##----------------------------- AUTHENTICATION TESTS ENDS ------------------------------##
