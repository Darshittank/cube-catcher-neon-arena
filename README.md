# 🎮 Cube Catcher – Neon Arena

A fast, polished 3D arcade game that runs in your browser. Slide the paddle, catch the falling neon cubes, dodge the red hazards, grab power-ups and chain combos for a high score.

**▶ Live demo:** [Play Now!! Cube Catcher](https://darshittank.github.io/cube-catcher-neon-arena/)

---

## ✨ Features

- Neon esports-style 3D arena built with [three.js](https://threejs.org/), with a bloom glow effect
- Smooth mouse, touch and keyboard controls, plus a paddle-speed slider
- Two modes: **3 Misses** (default, game over popup) and **Endless** (never ends)
- Five power-ups: Shield, Wide paddle, Slow-mo, Magnet and 2X Score
- Combo multiplier, level system and a saved best score
- Procedural background music and sound effects (no audio files) with sound, music and volume controls
- "Clean" and "Full" visual modes
- Works on desktop and mobile, and works **offline** because everything is inside one file

---

## 🕹️ How to play

Catch cubes with the paddle. Every cube you let fall to the floor is a miss. Red hazards must be avoided. Collect colored orbs for power-ups.

### Controls

| Action | Input |
|---|---|
| Move paddle | Mouse, touch drag, `←` `→` or `A` `D` |
| Start / restart | `Enter`, `Space` or the on-screen button |
| Pause / resume | `P`, `Esc` or the **Pause** button |
| Mute / unmute | **Sound** button (top right) |

The game also pauses automatically if you switch to another browser tab.

### Items

| Item | Effect |
|---|---|
| Colored cube | +10 points × current multiplier |
| Gold gem | +50 points × current multiplier |
| Red hazard | −25 points, combo reset (a Shield blocks it) |
| Shield (blue orb) | Blocks the next hazard or miss, lasts until used |
| Wide (green orb) | Paddle is 60% wider for 10 s |
| Slow-mo (purple orb) | Items fall slower for 8 s |
| Magnet (orange orb) | Pulls cubes toward you for 9 s |
| 2X Score (yellow orb) | Doubles all points for 10 s |

### Scoring, combo and levels

- Every 5 catches in a row adds +1 to the combo multiplier (up to x8, or x16 with 2X Score).
- A miss or hazard resets the combo.
- Every 10 catches you level up and the game speeds up. Difficulty levels off at about level 15, so long sessions stay playable.
- In **3 Misses** mode you lose a life for each missed cube, and reaching every 3rd level restores one life. At 0 lives the game over popup appears.
- In **Endless** mode there is no game over. Misses and hazards only cost 25 points and your combo.

### Settings (start and pause screens)

Mode, Sound, Music, Volume, Paddle speed and Visuals. Settings and your best score are saved in your browser (`localStorage`).

---

## 📁 Project structure

```
cube-catcher-neon-arena/
├── index.html            # The complete game (three.js is inlined). This is the file that gets deployed.
├── src/
│   └── game.src.html     # Readable source: HTML, CSS and game code without the inlined libraries
├── tools/
│   └── build.py          # Rebuilds index.html from src/game.src.html
├── .nojekyll             # Tells GitHub Pages to serve files as-is
├── .gitignore
├── LICENSE
└── README.md
```

**Only `index.html` is needed to play or deploy.** The `src/` and `tools/` folders are for editing the game.

---

## 💻 Run locally

No install is needed.

1. Download or clone the repository.
2. Double-click `index.html`. It opens in your browser and works offline.

Optional: serve it with a local web server.

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

---

## 🚀 Deploy to GitHub Pages (live demo)

### 1. Install Git and create a GitHub account

- Download Git from <https://git-scm.com/downloads>
- Sign up at <https://github.com>
- Tell Git who you are (one time only):

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### 2. Create the repository on GitHub

1. Click **+** (top right) → **New repository**.
2. Name it `cube-catcher-neon-arena`.
3. Set it to **Public** (required for free GitHub Pages on most accounts).
4. Do **not** tick "Add a README", "Add .gitignore" or "Add a license" (this project already includes them).
5. Click **Create repository**.

### 3. Push the project

Open a terminal inside the project folder and run (replace `YOUR-USERNAME`):

```bash
git init
git add .
git commit -m "Initial commit: Cube Catcher Neon Arena"
git branch -M main
git remote add origin https://github.com/Darshittank/cube-catcher-neon-arena.git
git push -u origin main
```

If GitHub asks for a password, use a **Personal Access Token** (GitHub → Settings → Developer settings → Personal access tokens) or sign in through GitHub Desktop or the browser prompt.

**No command line?** On the repository page click **Add file → Upload files**, drag in everything from the project folder, and click **Commit changes**.

### 4. Turn on GitHub Pages

1. Open the repository → **Settings** → **Pages** (left sidebar).
2. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
3. Choose branch **main** and folder **/ (root)**, then click **Save**.
4. Wait 1–2 minutes and refresh the page. A banner shows your live link:

```
https://Darshittank.github.io/cube-catcher-neon-arena/
```

### 5. Add the live link to your repository

1. On the repository home page click the ⚙️ next to **About**.
2. Paste your live URL into **Website** (or tick **Use your GitHub Pages website**) and save.
3. Edit the demo link at the top of this README with your real URL.

### Updating the game later

```bash
git add .
git commit -m "Describe your change"
git push
```

The live site refreshes automatically within a minute or two.

---

## 🛠️ Edit and rebuild

Edit `src/game.src.html`, then rebuild `index.html`:

```bash
npm install three@0.128.0
python3 tools/build.py
```

Handy values near the top of the game script in `src/game.src.html`:

| Constant | Meaning |
|---|---|
| `W` | Width of the play field |
| `BASEPW` | Paddle width |
| `MAXL` | Lives in 3 Misses mode |
| `PW` | Power-up colors, names and durations (seconds) |

Difficulty is controlled by the `speed()` and `interval()` functions, and item spawn odds by the `spawn()` function.

---

## 🧩 Tech stack

- [three.js r128](https://threejs.org/) (WebGL rendering, bloom post-processing), bundled into `index.html`
- Vanilla JavaScript, HTML and CSS
- Web Audio API for all music and sound effects
- Google Fonts (Orbitron, Rajdhani) are optional. The game falls back to system fonts when offline.

## 🌐 Browser support

Any modern browser with WebGL: Chrome, Edge, Firefox, Safari (desktop and mobile). Sound starts after your first click or key press, as browsers require.

---

## 🧰 Troubleshooting

| Problem | Fix |
|---|---|
| Live link shows 404 | Wait 2 minutes, confirm Pages is set to `main` / `(root)` and that `index.html` is in the repo root |
| Blank or black screen | Enable hardware acceleration / WebGL in your browser settings |
| No sound | Click the page once, check the **Sound** button isn't OFF and Volume isn't 0 |
| Game feels laggy | Switch **Visuals** to **CLEAN** and close other heavy tabs |
| Settings or best score reset | Your browser is blocking storage (private mode or cleared data) |
| `git push` rejected | Run `git pull origin main --rebase`, then push again |

---

## 🗺️ Ideas for the future

Online leaderboard, extra power-ups, boss levels, skins, gamepad support.

## 📄 License

[MIT](LICENSE). three.js is also MIT licensed.
