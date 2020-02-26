from django.test import TestCase
# , Client
from django.contrib.auth.models import User


# Create your tests here.
class AccountsTestCase(TestCase):

    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

    def api_is_active(self):
        """ Tests the slug generated when saving a Page. """
        # Author is a required field in our model.
        # Create a user for this test and save it to the test database.
        user = User()
        user.save()

        # Create and save a new page to the test database.
        response = self.client.get('/api/guru')

        # Make sure the slug that was generated in Page.save()
        # matches what we think it should be.
        self.assertEqual(response, 200)

    def api_can_update(self):
        """Test the api can update a given bucketlist."""
        person1 = User(name="test person1",
                       bio="test person1",
                       contact_info="test person")
        person2 = User(name="test person2",
                       bio="test person2",
                       contact_info="test person")
        person1.save()
        person2.save()
        # update_person = self.client.put(
        #     reverse('details', kwargs={'pk': person1.id}),
        #     person2, format='json'
        # )
        self.assertEqual(self.client.get('/api/guru'), 200)
