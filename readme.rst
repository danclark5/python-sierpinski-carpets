Sierpinski's Carpet Generation
==============================

This is a fun little script was created as a solution to a
`problem on the dailyprogrammer subreddit community <https://www.reddit.com/r/dailyprogrammer/comments/748ba7/20171004_challenge_334_intermediate_carpet/>`_
.

To run
------

It's a good practice to use virtualenvs to isolate package requirements. This script uses the following
packages:

 - attrs==17.2.0
 - Pillow==4.3.0

**Skip the following if you understand virtualenvs**

Assuming you have python you'll need to do the following. If you don't have python installed there are plenty of
resources, or you can send me a message on twitter. 

1. Create a virtualenv. This can be done with ``python -m venv nameofyourvirtualenv``
2. Create an environment variable to get to bin or scripts directory in the virtualenv
3. Upgrade pip in said virtualenv with ``$ve\pip install --upgrade pip``
4. Install requirements with ``$ve\pip install -r requirements.txt``

**Resume reading if you are skipping**

To run the scripts you simply invoke them with the python executable in your venv. No parameters needed. Just watch out when
you create a bmp. The script is still simplistic in that it just writes to the same file, so your **new images will
overwrite your old ones**.

An example command is ``$ve\python sierpinski_0.3.py``



