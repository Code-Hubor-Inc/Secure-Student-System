# Contributing to Secure Student System

First off, thank you for considering contributing to Secure Student System! It's people like you that make this project great.

## 🎯 How Can I Contribute?

### 🐛 Reporting Bugs
This section guides you through submitting a bug report. Following these guidelines helps maintainers understand your report, reproduce the behavior, and find related reports.

**Before Submitting A Bug Report**
- Check the [documentation](docs/) first
- Determine if your bug is really a bug
- Check if the issue has already been reported

**How to Submit a Good Bug Report**
- Use a clear and descriptive title
- Describe the exact steps to reproduce the problem
- Provide specific examples to demonstrate the steps
- Describe the behavior you observed and what you expected
- Include screenshots or animated GIFs if possible
- Include your environment details (OS, browser, versions)

### 💡 Suggesting Enhancements
This section guides you through submitting an enhancement suggestion.

**Before Submitting an Enhancement**
- Check if the enhancement has already been suggested
- Determine which component the enhancement relates to

**How to Submit a Good Enhancement Suggestion**
- Use a clear and descriptive title
- Provide a step-by-step description of the suggested enhancement
- Provide specific examples to demonstrate the steps or point
- Explain why this enhancement would be useful to most users
- List some other applications where this enhancement exists

### 🔧 Your First Code Contribution

**Setting Up Development Environment**
```bash
# 1. Fork and clone the repository

# 2. Clone your fork and add the original repository as upstream:
git clone https://github.com/yourusername/secure-student-system.git
cd secure-student-system

# 3. Add the original project as 'upstream'
git remote add upstream https://github.com/original/secure-student-system.git

# 4. Verify your remotes are set up correctly
git remote -v

# Should show:
# origin    https://github.com/YOUR_USERNAME/secure-student-system.git (fetch)
# origin    https://github.com/YOUR_USERNAME/secure-student-system.git (push)
# upstream  https://github.com/ORIGINAL_OWNER/secure-student-system.git (fetch)
# upstream  https://github.com/ORIGINAL_OWNER/secure-student-system.git (push)

# Install dependencies
./scripts/install-dependencies.sh

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Start development servers
docker-compose -f docker-compose.dev.yml up