import subprocess
import unittest

id_title_actual = [ "11b9a42c3f90e94fa6c5f43a51d27375ad1d8a75, Japanese economy contracts for third straight quarter",
                    "1594afb2392cc38bda662f1b40705d3484a2bd9f, Supermassive black hole weighed using new scale",
                    "10ade84e7d81290a6545f7e789f2f3ec53a53102, Horsemeat scandal: How often does food fraud happen?",
                    "16eec83012e9c0618224ec9b6cf25e414f049416, Brecon Beacons National Park wins dark sky status",
                    "34e29d6a1e1c49ab213700aa0b7807311350a1ff, China's Shenzhou-10 astronauts return to Earth",
                    "12f42a88ffbc9ce5c0e951a67b2fe53ef302b730, 'Every new car' connected to web by 2014",
                    "13c6aac61dc220fb6128bef673fa228e9102f71b, Lost in Thailand shakes up China's movie industry",
                    "b063dfcbd1fe5b6764a5f2e5af0478264328bba3, Richard Brooke: BT Sport deal 'will benefit viewer'",
                    "12c5e190772bb65a2b6ee84fe5391cf2612a4775, Peugeot Citroen reports record annual loss",
                    "14157c6dd69bf1b009064f36ea78dd3357816ca2, MLAs clash over St Patrick's Day Washington visit",
                    "145aee6d6d94b8f1e305c4d76dcfe4bd04e41b59, UK workers earning the same as they were ten years ago",
                    "7bd747b8ea5f0df625a99a68f0a6d0749bfe4ee3, India raises duty on gold jewellery imports",
                    "167fdcf6749c77bbb1813b6e292705c921d82104, Three charged in rhino horn smuggling ring",
                    "1005eb104f45e86e047221ffd54f93e90051bc46, Book of Mormon musical storms West End",
                    "11c8f377caa712b546d0c3e5ae18da5a18f54a26, South Yorkshire landslip rail line closed for weeks",
                    "1642a9711f05d27734849603d0f9cac510654be4, Samsung struggles to block iPhone function for the blind",
                    "15de5bbbee140015f22ac4afa435ced5e2fe02a3, Apple computers \'hacked\' in breach",
                    "114be37664500b42de5b5bd0f6d72220d91190a8, Sony to sell slimmer PlayStations to help boost sales",
                    "13d55cb49ce9bdbe97d938383e3be6cc1799ea85, Paralysed woman\'s thoughts control robotic arm",
                    "13a6d1dd560f542935da75869b892c4460ceae16, Carbon Trust launches scheme to tackle water waste"]

class tests(unittest.TestCase):

    def test_file_does_not_exist(self):

        out = subprocess.Popen(["python3", "search.py", "exercise_data2.csv", "hacking"], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT)
        stdout, stderr = out.communicate()
        self.assertEqual(stdout.decode("utf-8"),    "Error: file does not exist\n"+
                                                    "python3 search.py <csv> [search terms(s)...]\n")


    def test_insufficient_cli_arguments(self):
        
        out = subprocess.Popen(["python3", "search.py", "exercise_data.csv"], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT)
        stdout, stderr = out.communicate()
        self.assertEqual(stdout.decode("utf-8"),    "Error: insufficient command line arguments\n"+
                                                    "python3 search.py <csv> [search terms(s)...]\n")

    def test_both_errors(self):

        out = subprocess.Popen(["python3", "search.py", "exercise_data2.csv"], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT)
        stdout, stderr = out.communicate()
        self.assertEqual(stdout.decode("utf-8"),    "Error: insufficient command line arguments\n"+
                                                    "Error: file does not exist\n"+
                                                    "python3 search.py <csv> [search terms(s)...]\n")


    def test_simple_all_query(self):

        out = subprocess.Popen(["python3", "search.py", "exercise_data2.csv", "a"], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT)
        stdout, stderr = out.communicate()
        id_title_prog = stdout.splitlines()
        id_title_correct = id_title_actual
        self.assertTrue(id_title_prog.sort() == id_title_correct.sort())
    

    def test_specific_query(self):

        out = subprocess.Popen(["python3", "search.py", "exercise_data2.csv", "hacking"], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT)
        stdout, stderr = out.communicate()
        id_title_prog = stdout.splitlines()
        id_title_correct = [id_title_actual[5]] + [id_title_actual[16]]
        self.assertTrue(id_title_prog.sort() == id_title_correct.sort())
    

    def test_no_queries(self):

        out = subprocess.Popen(["python3", "search.py", "exercise_data2.csv", "decrement"], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT)
        stdout, stderr = out.communicate()
        id_title_prog = stdout.splitlines()
        id_title_correct = []
        self.assertTrue(id_title_prog.sort() == id_title_correct.sort())


    def test_multiple_queries(self):

        out = subprocess.Popen(["python3", "search.py", "exercise_data2.csv", "news", "hacking"], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT)
        stdout, stderr = out.communicate()
        id_title_prog = stdout.splitlines()
        id_title_correct = [id_title_actual[5]] + [id_title_actual[16]]
        self.assertTrue(id_title_prog.sort() == id_title_correct.sort())


    def test_case_insensitive(self):

        out_lower = subprocess.Popen(["python3", "search.py", "exercise_data2.csv", "boss"], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT)
        stdout_lower, _ = out_lower.communicate()
        id_title_lower = stdout_lower.splitlines()

        out_upper = subprocess.Popen(["python3", "search.py", "exercise_data2.csv", "BOSS"], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT)
        stdout_upper, _ = out_upper.communicate()
        id_title_upper = stdout_lower.splitlines()
        
        self.assertTrue(id_title_lower.sort() == id_title_upper.sort())

if __name__ == "__main__":
    unittest.main()