# 9_github_trending task

**Description**
--------
Script looks for 20 repositories created in the last week with a lot of stars, prints a link to the repository, the number of stars and open issues and links to them.
**Requirements**
--------
```
pip3 install -r requirements.txt
```
**Examples**
--------
```sh
$ python3 github_trending.py

==================================================
         Listing of community-curated resources to find topical remote freelance & contract work for software developers, web designers, and more!
https://github.com/engineerapart/TheRemoteFreelancer
--------------------------------------------------
        Stars: 1299
        Issues: 15
                 Added guru.com
         https://api.github.com/repos/engineerapart/TheRemoteFreelancer/issues/26
                 Fixes for typos
         https://api.github.com/repos/engineerapart/TheRemoteFreelancer/issues/25
                 fixing minor typo
         https://api.github.com/repos/engineerapart/TheRemoteFreelancer/issues/24
                 Fix typo
         https://api.github.com/repos/engineerapart/TheRemoteFreelancer/issues/23
                 Fix some links
         https://api.github.com/repos/engineerapart/TheRemoteFreelancer/issues/22
                 Remove highlights (bolding) for random companies
         https://api.github.com/repos/engineerapart/TheRemoteFreelancer/issues/21
                 Added Loom, a work-for-equity platform for entrepreneurs and developers
         https://api.github.com/repos/engineerapart/TheRemoteFreelancer/issues/20
                 Seven Days
         https://api.github.com/repos/engineerapart/TheRemoteFreelancer/issues/19
                 Remote Digest url
         https://api.github.com/repos/engineerapart/TheRemoteFreelancer/issues/18
                 Add Lightboard.io as freelance design resource.
         https://api.github.com/repos/engineerapart/TheRemoteFreelancer/issues/17
                 Added CodersClan and ordered the list
         https://api.github.com/repos/engineerapart/TheRemoteFreelancer/issues/16
                 Domino is now at https://www.wearedomino.com/freelancer
         https://api.github.com/repos/engineerapart/TheRemoteFreelancer/issues/14
                 Add Folyo.me 
         https://api.github.com/repos/engineerapart/TheRemoteFreelancer/issues/11
                 No license doesn't imply permission to use and modify
         https://api.github.com/repos/engineerapart/TheRemoteFreelancer/issues/9
                 Already a list at http://alternativeto.net/
         https://api.github.com/repos/engineerapart/TheRemoteFreelancer/issues/7
==================================================
         Dirty COW
https://github.com/dirtycow/dirtycow.github.io
--------------------------------------------------
        Stars: 903
        Issues: 9
                 Difference between various root access.
         https://api.github.com/repos/dirtycow/dirtycow.github.io/issues/27
                 Challenge: exploit on 1 CPU. Make a suitable code path sleep (& context-switch) at a right time
         https://api.github.com/repos/dirtycow/dirtycow.github.io/issues/26
                 Freezing computer few seconds after use 
         https://api.github.com/repos/dirtycow/dirtycow.github.io/issues/25
                 Challenge: exploit #DirtyCOW without MADV_DONTNEED
         https://api.github.com/repos/dirtycow/dirtycow.github.io/issues/21
                 Instructions and Testing
         https://api.github.com/repos/dirtycow/dirtycow.github.io/issues/18
                 Tighten up the graphics on #2 and #3 a little bit
         https://api.github.com/repos/dirtycow/dirtycow.github.io/issues/4
                 "All the boring bugs are way more important" is misleading
         https://api.github.com/repos/dirtycow/dirtycow.github.io/issues/3
                 "Am I affected by the bug?" is misleading
         https://api.github.com/repos/dirtycow/dirtycow.github.io/issues/2
                 refactored HTML
         https://api.github.com/repos/dirtycow/dirtycow.github.io/issues/1
...
```
