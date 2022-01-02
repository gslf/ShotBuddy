import unittest

from webapp.SessionsManager import SessionsManager

class TestSessionManagement(unittest.TestCase):
    
    def testList(self):
        # Load the session lists
        sm = SessionsManager(current_user_id = 1)
        result = sm.list()
        self.assertGreater(len(result), 0)


    def testLoadLast(self):
        # Load the last session
        sm = SessionsManager(current_user_id = 1)
        result = sm.loadLast()
 
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.id)

    def testSaveRemove(self):
        # Create a new session
        id_user = 1
        percentage_target = 1
        shots = "[1]"
        duration = 1

        sm = SessionsManager(current_user_id = 1)
        result = sm.new(id_user, percentage_target, shots, duration)
        self.assertTrue(result)

        # Edit and save the session
        sm.session.shots = "[1,2]"
        result = sm.save()
        self.assertTrue(result)

        # Check saved session
        result = sm.load(sm.session.id)
        self.assertEqual(result.shots, "[1,2]")

        # Remove the session
        result = sm.remove()
        self.assertTrue(result)
