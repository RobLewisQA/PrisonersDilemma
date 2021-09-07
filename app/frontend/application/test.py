from flask_testing import TestCase
from flask import url_for
import requests_mock
from application import app

class TestBase(TestCase):
    def initiate_app(self):
        return app

class TestFreegameRequests(TestBase):
    def test_freegame1_get(self):
        response = self.client.get(url_for('freegame1'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Create", response.data)
    
    def test_freegame1_post(self):    # testing the submission of a new product
        response = self.client.post(url_for('freegame1'),data = dict(cc_points=2,dd_points=1,cd_points=0,dc_points=4,rounds= 5,matches = 1,noise=0),follow_redirects=True)
        assert response.status_code == 200
        self.assertIn(b"Probability of misfiring: 0",response.data)
        self.assertIn(b"Number of rounds in a match: 5",response.data)
        self.assertIn(b"Number of matches per matchup in tournament: 5",response.data)
        #self.assertIn(b"['C_AlwaysC'-'D_AlwaysD']",response.data)


    # def test_freegame2_post-receipt(self): 
    #     with requests_mock.mock() as m:
    #         m.get("http://back-end:5000/freegame2", text = '{"prize":"no prize","rand_number":"401e","win_lose":"lose"}')
    #         response = self.client.get(url_for('frontend'))
    #         assert response.status_code == 200
    #         self.assertIn(b'lost', response.data)

    def test_freegame2_get(self):
        response = self.client.get(url_for('freegame2'))
        assert response.status_code != 200
    
    def test_freegame2_post(self):
        response = self.client.post(url_for('freegame2'),data = dict(cc_points=2,dd_points=1,cd_points=0,dc_points=4,rounds= 5,matches = 1,noise=0),follow_redirects=True)
        assert response.status_code == 200
        assert response.data != ""

