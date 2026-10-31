# Hojoon Lee

Personal website: https://joon0512.github.io/noojohworld/

An English-language portfolio with four project notes, teaching experience, a tutoring recording, and a short background. The site is static and runs on GitHub Pages.

## Edit and preview

```sh
python3 scripts/build.py
python3 scripts/check.py
python3 -m http.server 8765 --bind 127.0.0.1 --directory docs
```

Open http://127.0.0.1:8765.

- `scripts/build.py`: page templates, project content, and diagrams. Run it after editing content.
- `docs/style.css`: layout, responsive styles, and themes.
- `docs/app.js`: theme selection and video rendering.
- `docs/data/projects.json`: generated project data.
- `docs/data/videos.json`: video IDs, English titles, and optional duration labels. The build preserves this file.
- `scripts/check.py`: local links, anchors, asset paths, headings, and data validation.

The current recording is in Korean. Its surrounding website text is in English. Videos use YouTube's privacy-enhanced player and include a direct viewing link. An empty video list hides the section.

The text and project links work without JavaScript. Fonts fall back to system fonts if Google Fonts is unavailable.

## Deploy

Generated URLs include content versions to avoid mixing new pages with cached styles, scripts, or video data.

Commit the generated files. GitHub Pages serves `main` / `/docs` without an application server. The older `noojohojoon/` directory is outside the published site.

Project descriptions distinguish coursework, team work, and personal projects. Diagrams explain structure; they do not represent measured results.

## Design references

These 20 sites informed the earlier review of content and navigation. The current revision uses shorter English copy and a simpler layout.

1. [Dohyun Kim](https://dohyunkim02-portfolio.netlify.app/)
2. [Jihwan Park](https://aptheparker.work/en)
3. [kdy1](https://kdy1.dev/)
4. [Andrej Karpathy](https://karpathy.ai/)
5. [Julia Evans](https://jvns.ca/)
6. [Brittany Chiang](https://brittanychiang.com/)
7. [Lee Robinson](https://leerob.com/)
8. [Anthony Fu](https://antfu.me/)
9. [Guillermo Rauch](https://rauchg.com/)
10. [Josh W. Comeau](https://www.joshwcomeau.com/)
11. [Tania Rascia](https://www.taniarascia.com/)
12. [Simon Willison](https://simonwillison.net/)
13. [Lilian Weng](https://lilianweng.github.io/)
14. [Sebastian Raschka](https://sebastianraschka.com/)
15. [Dan Luu](https://danluu.com/)
16. [Brian Lovin](https://brianlovin.com/)
17. [Paco Coursey](https://paco.me/)
18. [Emil Kowalski](https://emilkowal.ski/)
19. [Arun Venkatesan](https://arun.is/)
20. [Maggie Appleton](https://maggieappleton.com/)
