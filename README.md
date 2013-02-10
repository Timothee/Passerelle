Passerelle
===

Passerelle is a Flask-based Python app that **takes one git URL, clone
it locally and push it to a second URL**.

I'm building this in the context of pushing a specific git repo to
Heroku from a Chrome extension. Since I can't push directly from a
browser (unless I rebuild a git client in Native Client, I guess?),
here is Passerelle.

How to use Passerelle
---

I'm just starting so I'm not entirely sure how it will work, but most
likely you'll have your Passerelle instance and will call it with
something that look like that:

    http://passerelle.example.com/?from=git@github.com%3ATimothee/Passeplat.git&to=git@heroku.com%3Apasserelle-heroku.git

and with some way to insure you're you and not anybody. Still TBD, but
I'd probably have a secret key set as environment variable that the
JavaScript client would also know and bim bam boom, we have something to
compare.


License
---

This code is provided under the MIT License.

(c) 2013 Timothée Boucher - timotheeboucher.com
