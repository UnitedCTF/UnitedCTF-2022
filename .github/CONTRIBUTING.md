# Contributions to UnitedCTF 2022

First of all, thank you for willing to contribute in making this event a memorable one.  

## Quick start

1. Fork the repository.  

2. Clone the forked repository:  

```bash
git clone https://github.com/${your_username}/UnitedCTF-2022
```

3. Configure upstream repository:  

```bash
git remote add upstream https://github.com/hfz1337/UnitedCTF-2022.git
```

4. Make sure to fetch from upstream first:  

```bash
git pull upstream master
git push origin master # to update your remote fork
```

5. Make a separate branch:  

```bash
git checkout -b add-{category_name}-{challenge_name}
```

6. Make changes locally.  

7. Add the affected files:  

```bash
git add category/challenge-name
```

8. Commit your changes:  

```bash
git commit
```

9. Push your changes:  

```bash
git push origin add-category-challenge-name
```

10. Make a pull request on Github.  

### Important note

**Always** pull from upstream before starting to make your local changes :  

```bash
git checkout master
git pull upstream master
git push origin master # to update your remote fork
```

## How to contribute

You can contribute in many different ways:

### Design a CTF challenge

You got a nice idea of a challenge that you want to add to the repository? Great, but before you do so, please consider some rules and guidelines first:

 - __Quality of the challenge:__ Do's & Don'ts:
   - __Don't__ plagiarize and submit challenges from past CTF contests, your challenge should be authentic. Instead, you can get some inspiration from them.
   - __Don't__ make a challenge that involves:
     - Guessing
     - Excessive brute forcing
     - Use of publicly available exploits (CVEs)
   - __Don't__ use spaces in directory and filenames, use dashes (**-**) or (exclusive) underscores (**_**) instead.
   - __Do__ create a separate directory for your challenge with a coherent name, and put it inside the appropriate category folder.
   - __Do__ initialize each challenge with a [`README.md`](./challenge-example/README.md) file and a [`challenge.yml`](./challenge-example/challenge/challenge.yml) file (to make its deployment easier with [ctfcli]).
   - __Do__ create a `solution` directory in your challenge's directory with a [`README.md`](./challenge-example/solution/README.md) in it. (this is where you put your write-up)
   - __Do__ write clean code for your challenge source code, this is highly appreciated.
   - __Do__ make a fun challenge that will teach or remind the player about an important concept.
   - __Do__ be creative in your challenge name, description and flag. The flag should be related to the challenge in some way.

 - __Submitting your challenge__: If your challenge respects the previous section, here's how to submit it:
   - Make a separate branch with a coherent name. (e.g. add-{category_name}-{challenge_name})
   - Commit and push the changes to the forked repository.
   - Open up a PR (Pull Request) so the challenge gets reviewed and tested before being merged to the main branch.

 - __Optional__: You can make work easier for us by:
   - Dockerizing your challenge. (mainly if it is a __pwn__ or __web__ challenge)
   - Testing your challenge and making sure it works as intended and there's no __easy__ unintended solution.
   - Making a write-up for the intended solution you had in mind while designing the challenge:
     - It should be written in markdown.
     - It should be put in the `solution/README.md` file of the challenge. 

Here's a table describing the impact of the amount of __work__ and __inspiration__ on the quality of a challenge:

| Tasks that need ⬇️+➡️ are | little work           | some work              | a lot of work        | too much work        |
|----------------------------|-----------------------|------------------------|----------------------|----------------------|
| __little inspiration__     | _Very easy_           | Relaxing/Disappointing | Uninteresting        | `Boring`             |
| __some inspiration__       | Easy/Satisfying       | Fun                    | Exhausting           | `Frustrating`        |
| __a lot of inspiration__   | Surprising/Insightful | Challenging            | _Very hard_          | `Very frustrating`   |
| __too much inspiration__   | `Guessy`              | `Frustrating`          | `Very frustrating`   | `Unreasonable`       |

Source: [ctf-design] page 10.

### Suggest a challenge idea

If you have a great challenge idea but don't have the chance to make it, it's fine! You can still suggest the idea so other contributors take it, enhance it and make a challenge out of it.  
To do so, open up a [new issue] and set the title to: "__challenge idea: brief description of the idea__", in the description, describe your challenge idea in details.

### Dockerize challenges

In case there are challenges that need be run inside a container but didn't get dockerized yet, you can write a Dockerfile for them and submit your PR.

### Enhancements

Review other contributors' challenges and suggest improvements for them, for example:
 - Cleaning, refactoring and reformatting the source code.
 - Fixing bugs in the challenge.
 - Other enhancements you judge being helpful.

### Challenge testing and write-ups

You can also contribute by testing challenges. To do so, you would have to deploy the challenge locally and solve it in __black box__, as if you were a CTF player who doesn't have access to the source code.  After solving the challenge, submit a write-up for it in __markdown__ syntax to be integrated in this repository.

### Other contributions

Any other way of contributing that comes into your mind!

## Thank you!

At the end, I want to say thank you again to everyone willing to contribute to this event, you're the best!

[new issue]:https://github.com/hfz1337/UnitedCTF-2022/issues/new
[ctf-design]:https://bit.ly/ctf-design
[ctfcli]:https://github.com/CTFd/ctfcli