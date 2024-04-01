import unittest
from switchkey.api.models.organization import SwitchKeyOrganization
from switchkey.core.exceptions import ResponseError


# TODO: Tests needs to be updated with auth logic.
class TestSwitchKeyOrganization(unittest.TestCase):

    def setUp(self):
        self.api = SwitchKeyOrganization()
        self.organization_id = None

    def test_create_organization_success(self):
        # Call the create method
        response = self.api.create(name="Test Organization")
        self.organization_id = response.id
        self.assertIsNotNone(response.id)

    def test_create_organization_invalid_data(self):
        with self.assertRaises(ResponseError):
            # Creating organization with the same name will raise an error because of the unique identity
            self.api.create(name="Test Organization")

    # def test_update_organization_success(self):
    #     # Prepare mock data
    #     updated_organization_data = SwitchKeyOrganizationResponseType(
    #         id=1,
    #         name="Updated Organization",
    #         owner=SwitchKeyUserResponseType(id=1, username="owner_username", email="owner@example.com"),
    #         members=[SwitchKeyUserResponseType(id=2, username="member1_username", email="member1@example.com")],
    #         created="2024-03-28T12:00:00Z",
    #         modified="2024-03-29T12:00:00Z"
    #     )
    #     # Call the update method
    #     response = self.api.update(updated_organization_data)
    #     # Assert that the response is None, indicating success
    #     self.assertIsNone(response)

    # def test_update_organization_invalid_data(self):
    #     # Prepare invalid organization data (missing required fields)
    #     invalid_organization_data = SwitchKeyOrganizationRequestType(
    #         name="Updated Organization",
    #         members=[]
    #     )
    #     # Call the update method with invalid data
    #     with self.assertRaises(TypeError):
    #         self.api.update(invalid_organization_data)

    # def test_delete_organization_success(self):
    #     # Prepare mock organization ID
    #     organization_id = 1
    #     # Call the delete method
    #     response = self.api.delete(organization_id)
    #     # Assert that the response is None, indicating success
    #     self.assertIsNone(response)

    # def test_get_organization_success(self):
    #     # Prepare mock organization ID
    #     organization_id = 1
    #     # Call the get method
    #     organization = self.api.get(organization_id)
    #     # Assert that the organization object is not None
    #     self.assertIsNotNone(organization)
    #     # Assert that the organization ID matches the expected value
    #     self.assertEqual(organization.id, organization_id)

if __name__ == '__main__':
    unittest.main()
