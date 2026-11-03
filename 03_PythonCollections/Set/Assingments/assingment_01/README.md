# Assignment 1: Sets - Deduplication, Membership & Methods

## Overview
This assignment introduces unordered collections of unique elements. We are building an access control whitelist auditor and a unique vocabulary stream inspector to handle automatic deduplication and membership lookups.

## Core Terms & Concepts Explained
* **Sets:** Unordered, unindexed collections enclosed in curly braces `{}` that strictly enforce uniqueness.
* **Automatic Deduplication:** Converting a list with duplicates into a set instantly removes all repeating values.
* **Set Mutations:** 
  * `.add(item)`: Inserts a single unique element.
  * `.remove(item)`: Deletes an element but crashes with a `KeyError` if the item is missing.
  * `.discard(item)`: Safely deletes an element without crashing if it does not exist.
* **Membership Testing:** Extremely fast checks using `in` and `not in` to verify if a specific item exists in the collection.

## Task Breakdown
**Task 1: Access Control Whitelist Auditor**
We convert a raw log of duplicate logins into a clean set. The script adds new authenticated users, revokes access using `.remove()`, and proves the safety of `.discard()` when removing non-existent user IDs.

**Task 2: Unique Vocabulary Stream Inspector**
We process a raw text stream by splitting it into tokens and casting it into a set to eliminate duplicate words. The script then verifies the presence of specific keywords in the final vocabulary pool.