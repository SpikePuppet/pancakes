# Pancakes - First Principles

## Overview

There are ultimately two problems I want to solve:
1. I want to be able to use stacked PRs in Git. This is notoriously difficult. Not necessarily because it can't be done, but because it's a bit strange. You have to stack the branches on top of each other. You have to merge them down in the correct order. It's a bit weird.
2. Most startups still use Git. While there are different alternative VCS systems that you can use, most startups will still use Git, and you don't always have access to really cool tools like Graphite. 

What I want to do here is make a simple tool to manage stacked PRs. The tool is meant to be a subset of things you can do in git. You're not meant to be able to do everything. You're not meant to be able to cherry pick and rebase and all that kind of stuff. What you need to be able to do is the following:
1. Open a new branch.
2. Add commits to that branch.
3. Open stacked PRs.
4. Restack the PRs. 
5. merge PRs down one branch. 

### Note on this document

This document is my attempt to break down a problem I'm facing down to first principles. It might not be perfect and it might not be great, but it's intended to display how I was thinking about a project at the time and what I was planning to do. 