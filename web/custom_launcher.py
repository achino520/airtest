#coding=utf-8

from airtest.cli.parser import runner_parser
from airtest.cli.runner import AirtestCase, run_script



class CustomAirtestCase(AirtestCase):

    def setUp(self):
        print("custom setup")
        # add var/function/class/.. to globals
        # self.scope["hunter"] = "i am hunter"
        # self.scope["add"] = lambda x: x+1

        # exec setup script
        super(CustomAirtestCase, self).setUp()

    def tearDown(self):
        print("custom tearDown")
        # exec teardown script
        super(CustomAirtestCase, self).setUp()


if __name__ == '__main__':
    ap = runner_parser()
    args = ap.parse_args()
    run_script(args, CustomAirtestCase)