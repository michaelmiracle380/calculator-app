# Calculator App — Build & Install Guide

This is a Kivy-based Python calculator app, packaged to build into an Android APK
using GitHub Actions (cloud build) — no Android SDK/NDK needed on your phone.

## What's in this folder
- `main.py` — the calculator app (buttons, +, -, *, /, ^, sqrt, %, parentheses)
- `buildozer.spec` — Android build config
- `icon.png` — placeholder app icon (swap with your own 512x512 PNG anytime)
- `.github/workflows/build.yml` — builds the APK automatically in the cloud

---

## Step 1: Create a free GitHub account
If you don't have one: https://github.com/signup

## Step 2: Create a new repository
1. Go to https://github.com/new
2. Name it e.g. `calculator-app`
3. Set it to **Public** (private also works, just easier public)
4. Do NOT initialize with a README (we already have files)
5. Click **Create repository**

## Step 3: Push this code from Termux

In Termux, install git if you don't have it:
```bash
pkg install git
```

Then, from inside this `calc-app` folder:
```bash
cd calc-app
git init
git add .
git commit -m "Initial calculator app"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/calculator-app.git
git push -u origin main
```

GitHub will ask you to log in — use a **Personal Access Token** as the password
(GitHub no longer accepts your account password for git pushes).

To create one: GitHub.com → Settings → Developer settings → Personal access tokens
→ Generate new token (classic) → check the `repo` box → Generate → copy it and
paste it as your password when Termux asks.

## Step 4: Watch the build run
1. Go to your repo on GitHub.com
2. Click the **Actions** tab
3. You'll see "Build Android APK" running (takes ~15-20 minutes the first time)
4. When it finishes with a green checkmark, click into the run

## Step 5: Download the APK
1. Still inside that workflow run, scroll to **Artifacts**
2. Download `calculator-apk` (it's a zip containing your `.apk`)
3. Unzip it — that `.apk` file is your installable Android app

## Step 6: Install it on your phone
- Transfer the APK to your phone (if built on a separate device) or download
  directly from GitHub on your phone
- Tap the APK file to install (you may need to enable "Install unknown apps"
  for your browser/file manager in Android settings)

---

## Publishing to the Play Store (separate from this build)

The APK above is great for testing, but the Play Store requires:

1. **Google Play Developer account** — one-time $25 fee at
   https://play.google.com/console/signup
2. **A signed release build**, not the debug APK from this workflow. Change
   the workflow to run `buildozer android release` instead of `debug`, and
   set up a signing keystore (Buildozer docs cover this:
   https://buildozer.readthedocs.io/en/latest/)
3. **Play Console listing**: app description, screenshots, privacy policy URL,
   content rating questionnaire, etc.
4. Google reviews new apps before they go live — can take a few days.

I can help you prep the release build and signing config when you're ready
for that step — just ask.

## Making changes later
Edit `main.py`, then:
```bash
git add .
git commit -m "your change"
git push
```
The Actions workflow rebuilds automatically every time you push.
