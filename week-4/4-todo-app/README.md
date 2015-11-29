# Thursday - Todo console application

## Before lesson materials

Mandatory:

None. :wink:

Optional:

* [argparse][1] for command-line argument parsing

## Tasks

Write a command-line todo application to easily keep track of your day-to-day tasks.

### Functional requirements

Basics (_mandatory_):

* A todo item has (at least) a `completed` state and a description
* Load todo items on application start
* Save todo items on application exit
* Add new items
* Complete items
* Remove items
* List items

Advanced (optional):

* Remove all completed items
* Add search functionality for items
* Add due date to items
* Sort items by due date
* Add priority to items
* Sort items by priority
* Handle multiple lists of items
* Support multiple item states (such as todo, in-progress, done)
* Boost user experience with [curses][2]

### Tips

* Use a simple text file to store items, every line is an item.
* To support more advanced features use a semi-structured format like JSON or CSV.
* Turn the application into a full-fledged [CLI][3] application by providing `--help`

[1]: https://docs.python.org/3.5/library/argparse.html#module-argparse
[2]: https://docs.python.org/3/howto/curses.html
[3]: https://en.wikipedia.org/wiki/Command-line_interface
