# *Contributing ID*

***Contributor***

We are thrilled that you have chosen to contribute to this simple project. We welcome any changes you make, whether they are minor or significant. However, please adhere to the following rules:

- All work you submit must be your own and should not infringe on anyone else's copyright. Please provide references if you take from others.
- Your contributions will be licensed under the [MIT](LICENSE) license once your pull request has been merged.
- Your work must comply with our coding standards and style guidelines.
- You are not permitted to use the `main` branch for pull requests.

# *Pull Request*

***Good Pull Request***

- First, fork our repository.
- Then, clone the repository you forked.
    ```bash
    git clone https://github.com/<username>/<repository>.git
    ```
- Install `pre-commit` if you haven't already.
    ```bash
    pip install pre-commit  # if not already installed
    pre-commit install
    ```
- Create a new branch; it is not advisable to use the default branch (our default branch is `main`).
    ```bash
    git checkout -b <your_branch_name>
    ```
- Make the changes you desire.
- Then, add the changes using `git add`.
- Commit your changes with `git commit`.
    ```bash
    git commit -m "feat: add the latest feature to phantom"
    ```
  
  **Suggested commit message formats**:
  - `feat:` for adding algorithms or other features;
  - `fix:` for modifying existing algorithms or fixing issues;
  - `docs:` for changing or creating documentation;
  - `add:` for adding algorithms or other features (optional);

  Note: The commit message should briefly explain the changes.

  Correct examples:
   - &#9746; feat: test_x.py
   - &#9745; feat: add the latest feature to phantom

  For more details, you can refer to:
   - [EN](https://www.conventionalcommits.org/en/v1.0.0/)
   - [ID](https://www.conventionalcommits.org/id/v1.0.0/)

- Finally, push to your branch.
    ```bash
    git push origin <your_branch_name>
    ```

Your pull request will be merged if:

- It adheres to the standards and guidelines set forth in `CONTRIBUTING.md`.

**Additional Notes**:

- If you encounter any issues or problems with your pull request, you can report the issues in the [issue tracker](https://github.com/dapuntech/phantom/issues).
- If there are tests that fail, we will review your changes.

For your pull request, please provide a detailed explanation of what you changed or added, and maintain a polite tone while expressing gratitude. This is a form of good etiquette towards fellow contributors and other programmers.

