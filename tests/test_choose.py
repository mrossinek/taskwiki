from tests.base import IntegrationTest
from time import sleep


class TestChooseProject(IntegrationTest):

    viminput = """
    * [ ] test task 1  #{uuid}
    * [ ] test task 2  #{uuid}
    """

    vimoutput = """
    * [ ] test task 1  #{uuid}
    * [ ] test task 2  #{uuid}
    """

    tasks = [
        dict(description="test task 1", project="Home"),
        dict(description="test task 2"),
    ]

    def execute(self):
        self.client.normal('2gg')
        sleep(1)

        self.command("TaskWikiChooseProject")
        sleep(1)

        self.client.normal('5gg')
        sleep(0.5)
        self.client.feedkeys("\\<CR>")
        sleep(1)

        for task in self.tasks:
            task.refresh()

        assert self.tasks[0]['project'] == "Home"
        assert self.tasks[1]['project'] == "Home"


class TestChooseProjectUnset(IntegrationTest):

    viminput = """
    * [ ] test task 1  #{uuid}
    * [ ] test task 2  #{uuid}
    """

    vimoutput = """
    * [ ] test task 1  #{uuid}
    * [ ] test task 2  #{uuid}
    """

    tasks = [
        dict(description="test task 1", project="Home"),
        dict(description="test task 2"),
    ]

    def execute(self):
        self.client.normal('1gg')
        sleep(0.5)

        self.command("TaskWikiChooseProject")
        sleep(0.5)

        self.client.normal('4gg')
        sleep(0.5)
        self.client.feedkeys("\\<CR>")
        sleep(0.5)

        for task in self.tasks:
            task.refresh()

        assert self.tasks[0]['project'] == None
        assert self.tasks[1]['project'] == None


class TestChooseProjectCanceled(IntegrationTest):

    viminput = """
    * [ ] test task 1  #{uuid}
    * [ ] test task 2  #{uuid}
    """

    vimoutput = """
    * [ ] test task 1  #{uuid}
    * [ ] test task 2  #{uuid}
    """

    tasks = [
        dict(description="test task 1", project="Home"),
        dict(description="test task 2"),
    ]

    def execute(self):
        self.client.normal('1gg')
        sleep(0.5)

        self.command("TaskWikiChooseProject")
        sleep(0.5)

        self.client.normal('4gg')
        sleep(0.5)
        self.client.feedkeys("q")
        sleep(0.5)

        for task in self.tasks:
            task.refresh()

        assert self.tasks[0]['project'] == "Home"
        assert self.tasks[1]['project'] == None

