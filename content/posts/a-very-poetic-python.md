---
title: "A very poetic Python 🐍"
date: 2022-06-06T13:26:54+02:00
draft: true
---

I have been using Python for all sorts of things in the past years.
Data science, music, scripting, automation, puzzle solving, web UI apps, serverless apps and more.
Yet throughout all this time I've constantly changed the ways in which I setup Python itself, virtual environments for my projects, package managers and all the peripherals of the POSIX world.
{{< marginnote >}}
Aliases, environment variables, shell scripts, dotfiles etc.
Also, [here's a nice article about what POSIX is](https://www.baeldung.com/linux/posix).
{{< /marginnote >}}

Throughout my adventures in Python I've been blessed
{{< marginnote >}}
Unfounded opinion based on observing conversations around the Python community,
stale 10-year old Python answers on StackOverflow,
a [countdown timer to Python2.7 end-of-life](https://pythonclock.org/) and more.
{{< /marginnote >}}
to have never used a pre-Python3 version.

Today I'm writing this post through a macOS device for which Apple has [decided to drop support for Python2.7](https://developer.apple.com/documentation/macos-release-notes/macos-12_3-release-notes#Python)
{{< marginnote >}}
I will actually update to macOS 12.3 Monterey through the writing of this post. 🤷‍♂️🤞
{{< /marginnote >}}
by not including any version of Python at all,
{{< marginnote >}}
It used to be installed by default in macOS under
`/usr/bin/python`
which was symlinked to the relevant binary under
`/System/Library/Frameworks/Python.framework/`
{{< /marginnote >}}
effectively giving the user full control over how they wish to install Python.

## And so it begins

Starting off with a test, I wanted to see if there is a `python`
command left in my terminal and to my surprise there was.
Seems like a symbolic link was left behind in `/usr/local/bin/python`, pointing to
`/usr/bin/python3`.
What was really odd though is that when I ran `python` I got a prompt from the system
{{< marginnote >}}
![xcode python cli developer tools install](/media/20220319-a-very-poetic-python/xcode-python-cli-developer-tools-install.png)
{{< /marginnote >}}
telling me that I need to install the _command line developer tools_ in order to run `python`.
I'm like _whaaa? okay install I guess?_ 🤷‍♂️

To nobody's surprise this did absolutely nothing.
A short investigation led me to not much more than suspicion that _[brew](https://brew.sh/)_
or some other little hack I had to do resulted in that symbolic link
{{< marginnote >}}
`/usr/local/bin/python -> /usr/bin/python3`
{{< /marginnote >}}
and deleting it
{{< marginnote >}}
`rm /usr/local/bin/python`</br>
Also did a _`brew cleanup`_ just in case, but I got nothing relevant to report.
{{< /marginnote >}}
didn't seem to affect my system, so _hurray!_

Now, of course you noticed that there is already a _Python_ version installed in my system.
![python3 version](/media/20220319-a-very-poetic-python/python3-version.png)

That is because well I only updated my device to _macOS 12.3_
{{< marginnote >}}
Actually <u>12.3.1</u> as I'm writing this.
Yes, I had time to update my device but not to finish this blog post and the process of reinstalling Python.
Thanks for noticing.
{{< /marginnote >}}❤️.

I didn't get a fresh new OS install or device for that matter.
Essentially, this means that my system will still have most of whatever dependencies it had before the update.
Now, of course I could go on and completely purge _Python_ for real
{{< marginnote >}}
![brew python uninstall](/media/20220319-a-very-poetic-python/brew-python-uninstall.png)
As in
`brew uninstall --ignore-dependencies python`
{{< /marginnote >}}
but that would introduce more trouble than I'm willing to go through, I hope you understand.

Testing one last thing before we continue, I recreated the symbolic link that we saw existed before
and it seems to be triggering the same _command line developer tools_ prompt.
![python recreating](/media/20220319-a-very-poetic-python/python-recreating.png)
Maybe something to report to _Apple_? Smells like a hardcoded thing to me.

```text
Work in progress! Come back for more later ❤️
```

---

{{< blockquote cite="" footer="Update 1" >}}
I managed to upgrade to 12.3 just fine, but I have yet to purge my Python setup.
{{< /blockquote >}}

{{< blockquote cite="" footer="Update 2" >}}
I finally got some time to continue, now I have purged most Python versions and their peripherals from my system.
Almost fresh start! Almost too fresh, while deleting things I accidentally ran `rm -rf ~/Library/`
instead of `rm -rf ~/Library/Python`. I realized it early and cancelled it
but I have no way to know if I deleted anything crucial...
A restart will tell.
{{< /blockquote >}}

{{< blockquote cite="" footer="Update 3" >}}
I managed to get some more progress on this post! 🥳 </br>
To be frank, I am using this post to document my progress in this task in real-time,
but my procrastination brain enjoys getting distracted with other improvements
on this personal blog. </br>
_Two birds with one stone_ you could argue! </br>
Only if the stone was thrown from the surface of the moon and the birds are sitting
on a tree on Earth. </br>
Ah well, stay tuned! 👾
{{< /blockquote >}}
