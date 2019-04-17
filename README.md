# LOGS ANALYSIS TOOL

Python tool that returns three reports from the _news_ database:

- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

**How to run the program**

Note: .gitignore file includes .sql format, you'll need to download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). The file inside is **newsdata.sql**.
This program was created in and runs on Vagrant and VM environment with Python 2.7. You'll need Vagrant (`vagrant init`, `vagrant up` and `vagrant ssh` in your terminal to start work in environment) and VM and load newsdata.sql file in your vagrant directory.

To load the data while in your vagrant directory use: `psql -d news -f newsdata.sql`. This will get the PostgreSQL terminal program running and connect the database.

Once you've completed this simply run: `python logs-analysis` in a separate terminal to have reports returned.

**Tools needed**
[Vagrant](https://www.vagrantup.com/)
[Virtual Machine](https://www.virtualbox.org/)
Terminal
