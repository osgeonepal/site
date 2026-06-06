# Contributing to OSGeoNepal

## **Prerequisites**

Before you start your journey, make sure you have the following:

- GitHub Account: Create a GitHub account if you don't have one. You'll use this account to interact with repositories, raise issues, and submit pull requests.
- Git Installed: Install Git on your local machine. This is essential for cloning repositories, making changes, and pushing them back to GitHub.
- Familiarity with Git: Basic knowledge of Git commands is beneficial. Learn about commands like clone, branch, commit, push, and pull request.
- Committer Responsibilities Guidelines - Make sure to follow these [OSGeo contributor guidelines](https://wiki.osgeo.org/wiki/Committer_Responsibilities_Guidelines).
- Community Standards - Make sure you have gone through our [OSGeo Nepal community standards](./Standards.md)

## **How to get started**

### **Finding the issue**

- Find the issue: Explore the OSGeoNepal repositories, and find the issue that piques your interest.
- Filter by Labels: Use labels like "beginner-friendly" or "good first issue" to indicate tasks suitable for newcomers. Look for these labels when searching for issues.
- Read the Documentation: Go through the project's README and contributing guidelines to understand the project structure, coding conventions, and how to contribute.

- Register you interest: After you find the issue, register your interest to inform others/maintainers that you are interested in that particular issue.
- Assign: After that maintainer assigns you to the issue, or ask to assign yourself.
- Proper Labeling: To begin contributing, add the label _Work in progress_.

### **Forking the repository**

- Fork the repository: On the project's GitHub page, click the "Fork" button to create your copy of the repository. This allows you to work on changes without affecting the original project.
- Clone your forked repository: Clone the forked repository to your local machine using the git clone command.

```bash
git clone https://github.com/your-username/repository.git

```

### **Make changes**

- Create a new branch: Create a new branch in the repository that you cloned in your local machine. This is to keep your main branch clean and allows you to work on multiple features.

```bash
git checkout -b <feature-name>

```

- Make Changes: Implement the changes or fixes you want to contribute.
  _Follow the coding standards and guidelines mentioned in the project's documentation._
- Commit Changes: Commit your changes with a descriptive commit message.

```bash
git add .
git commit -m "Add feature or fix"

```

- Push Changes: Push your changes to your cloned GitHub repository.

```bash
git push origin <feature-branch>

```

### **Creating the pull request**

- Open pull request (PR): Go to your GitHub repository, switch to your <feature-branch> (that you pushed), and click on the "New Pull Request" button.



#### Follow Pull request template: 
  - In order to add pull request template simple add `?template=default.md` in your PR URL for Eg : 
    ```
    https://github.com/osgeonepal/osgeonepal.github.io/compare/event/PR?template=events.md
    ```

- Describe your changes: Write a clear and concise description of the changes you made.
  _Reference any related issues_
- Review process: Address the feedback that the project maintainer provide if any.
- Merge pull request: Once your changes are approved, the maintainers will merge your pull request into the main project.

**_Congratulations! You have just contributed to the OSGeoNepal on GitHub._**
