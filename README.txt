SCAN2PDF - how to use and turn it into an APK / Play Store app
================================================================

FILES
  index.html, sw.js, manifest.webmanifest, icon-*.png  -> the app
  privacy.html                                         -> privacy policy (edit your email in it)
  make_icons.py                                        -> optional, regenerates icons

IMPORTANT: a PWA needs to be served over HTTPS (camera, install and offline
mode do not work when you just open the file). So host it first.

STEP 1 - HOST IT FREE (pick one, easiest first)
  Netlify Drop:  go to app.netlify.com/drop, drag the UNZIPPED folder in.
                 You instantly get a https://xxxx.netlify.app link.
  GitHub Pages:  create a repo, upload all files, Settings > Pages > deploy from main.

STEP 2 - TEST ON YOUR PHONE
  Open the link in Chrome on Android. Tap the Install button in the app header
  (or Chrome menu > "Add to Home screen"). It now works like a normal app, offline too.

STEP 3 - MAKE THE APK / AAB
  1. Go to pwabuilder.com and paste your link.
  2. Click Package for stores > Android.
  3. Fill in the package ID (e.g. com.yourname.scan2pdf), app name, etc.
  4. Download. You get an .apk (to share directly) and an .aab (for Play Store),
     plus a signing key file. KEEP THE SIGNING KEY SAFE - you need it for every update.

STEP 4 - PLAY STORE (optional)
  - Google Play Console account ($25 one time), identity verification.
  - Upload the .aab, add icon, screenshots, description.
  - Privacy policy URL: your-link/privacy.html
  - New personal accounts normally need a closed test (about 12 testers, 14 days)
    before public release - check Google's current rules.

USING THE APP
  Camera button: scan a page -> crop -> pick a filter (Magic / Gray / B&W) -> Done.
  Gallery: pick many photos at once.
  Arrows move pages, pencil edits, bin deletes.
  Save PDF: choose name, A4 or fit-to-image, quality -> Create -> Share / Download.
