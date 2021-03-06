import os
import textwrap

import pytest


def test_foo_dry_run(command_tester_factory):
    command_tester = command_tester_factory("generate")
    with pytest.raises(SystemExit) as pytest_wrapped_exit:
        command_tester.execute("-d -w repos/foo")
    assert pytest_wrapped_exit.type == SystemExit
    assert pytest_wrapped_exit.value.code == os.EX_OK
    assert (
        "poetry init --dependency=scrapy --dependency=beautifulsoup4 --dev-dependency=pytest --license=MIT"
        in command_tester.io.fetch_output()
    )


@pytest.mark.skip(reason="Currently, subprocess returns returncode 1.")
def test_foo(command_tester_factory):
    command_tester = command_tester_factory("generate")
    command_tester.execute("-w repos/foo", inputs="no\nno")
    msg = textwrap.dedent(
        """\
        Generated init command:

        poetry init --dependency=scrapy --dependency=beautifulsoup4 --dev-dependency=pytest --license=MIT


        Execute the above command. Also, the following output is due to Poetry.
        """
    )
    assert msg in command_tester.io.fetch_output()
