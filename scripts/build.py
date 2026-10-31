from pathlib import Path
import html
import json

root = Path(__file__).resolve().parents[1]
docs = root / 'docs'
(docs / 'work').mkdir(exist_ok=True)
projects = [
    {
        'id': 'proc-lens', 'name': 'proc-lens',
        'sub': 'A Linux process snapshot module',
        'tech': 'C · Linux · QEMU', 'scope': 'Personal project',
        'summary': "A Linux kernel module that keeps process snapshots stable while they're being read.",
        'intro': 'A Linux kernel module that periodically collects process information and keeps a snapshot stable for each open file.',
        'points': [
            ('How it works', 'A delayed_work task collects process data. Reference counting and locking manage object lifetimes, while each open file retains its snapshot even when a newer one is published.'),
            ('Checks', 'The repository documents QEMU checks for partial reads, seek, concurrent readers, process creation and exit, and 50 load/read/unload cycles. The test environment is Ubuntu Linux 6.8.0-147-generic on x86-64.'),
            ('Limits', 'A stable snapshot does not mean every field was captured at the same instant: RSS and scheduler values can change during collection. KASAN, lockdep, and allocation-failure injection have not been tested.')
        ],
        'links': [('Code', 'https://github.com/JOON0512/proc-lens'), ('Development notes', 'https://github.com/JOON0512/proc-lens/blob/main/docs/development.md')]
    },
    {
        'id': 'gshare', 'name': 'Gshare in gem5',
        'sub': 'Comparing branch predictor indexing',
        'tech': 'C++ · gem5 · RISC-V', 'scope': 'Team capstone · 2025',
        'summary': 'Compared four indexing operations in a Gshare branch predictor using gem5.',
        'intro': "We compared XOR, OR, AND, and XNOR indexing in a Gshare predictor on gem5's RISC-V O3CPU.",
        'points': [
            ('Experiment', 'We kept the prediction table and counter configuration fixed and ran graph workloads. We compared branch mispredictions per thousand instructions (MPKI) alongside instructions per cycle (IPC).'),
            ('Takeaway', 'The results depended on the workload. Comparing MPKI and IPC together helped us see how changes in prediction behavior related to execution performance.')
        ],
        'links': [], 'source_note': 'Based on our course report, which is not publicly available.'
    },
    {
        'id': 'xv6', 'name': 'xv6-riscv labs',
        'sub': 'Scheduling, memory, and threads',
        'tech': 'C · RISC-V · QEMU', 'scope': 'Coursework · 2024',
        'summary': 'Exercises in system calls, scheduling, copy-on-write, and threads using xv6-riscv.',
        'intro': 'Operating systems coursework built on MIT xv6-riscv and the course starter code.',
        'points': [
            ('Exercises', 'The assignments cover shell behavior, system calls, stride scheduling, copy-on-write, memory allocation, and threads. They helped me trace a request from user code into the kernel and follow how scheduling and memory policies affect execution.'),
            ('Testing', 'The repository includes assignment code and run instructions. The documented checks use one CPU; multicore synchronization and scheduling fairness need separate verification.')
        ],
        'links': [('Code and run instructions', 'https://github.com/JOON0512/yonsei-OS')]
    },
    {
        'id': 'zynq', 'name': 'Zynq board labs',
        'sub': 'Interrupts, memory, and device drivers',
        'tech': 'C · Zynq · MMIO', 'scope': 'Coursework · 2026',
        'summary': 'Board exercises covering interrupts, BRAM, display control, and Linux device drivers.',
        'intro': 'Embedded systems coursework on a Zynq board, using the supplied IP, BSP, and examples.',
        'points': [
            ('Exercises', 'I worked with button interrupts, LED patterns, BRAM, and a TFT-LCD. Interrupt handlers updated state, while the main loop handled output. Other exercises used memory-mapped I/O and a character device driver to connect user programs to the board.'),
            ('Observation', 'A busy-wait in the output loop can affect responsiveness even when interrupts are handled correctly. Following the whole path from input to output made that distinction easier to see.')
        ],
        'links': [('Lab code', 'https://github.com/JOON0512/yonsei-embedded-systems')]
    }
]


def link(text, url, cls=''):
    return f'<a class="{cls}" href="{html.escape(url)}" target="_blank" rel="noopener noreferrer">{text}<span aria-hidden="true"> ↗</span></a>'


def head(title, desc, prefix=''):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#fafaf8"><meta name="description" content="{html.escape(desc, quote=True)}">
<meta property="og:title" content="{html.escape(title, quote=True)}"><meta property="og:description" content="{html.escape(desc, quote=True)}">
<title>{html.escape(title)}</title><link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{prefix}style.css"><script src="{prefix}app.js" defer></script>
</head>
<body><a class="skip" href="#main">Skip to content</a>'''


def header(prefix=''):
    home = prefix + 'index.html' if prefix else '#home'
    return f'''<header class="header wrap">
<a class="brand" href="{home}" aria-label="Hojoon Lee, home">Hojoon Lee</a>
<nav aria-label="Main navigation"><a href="{prefix}index.html#work">Work</a><a href="{prefix}index.html#teaching">Teaching</a><a href="{prefix}index.html#about">About</a></nav>
<button class="theme-toggle" type="button" aria-label="Switch to dark mode" hidden><span aria-hidden="true">◐</span></button>
</header>'''


def footer(prefix=''):
    return f'''<footer class="footer wrap"><span>© 2026 Hojoon Lee</span><a href="{prefix}index.html#home">Back to top ↑</a></footer></body></html>'''


def visual(id):
    if id == 'proc-lens':
        return '''<div class="snapshot-diagram" role="img" aria-label="Processes are collected into snapshots. Each reader keeps the same generation until it closes the file."><div class="diagram-top mono">PROCESS SNAPSHOT</div><div class="processes"><span>task A</span><span>task B</span><span>task C</span></div><div class="connector">↓ <span>delayed_work</span></div><div class="snapshot-box"><span class="mono">GENERATION n</span><div class="data-lines"><i></i><i></i><i></i><i></i></div><b>Process snapshot</b></div><div class="snapshot-bottom mono">open → read → close</div></div>'''
    if id == 'gshare':
        return '''<div class="logic-diagram" role="img" aria-label="The branch address and global history form an index into the prediction table."><div class="logic-input"><span>Branch PC</span><span>Global history</span></div><div class="connector">↓</div><div class="operators"><b>XOR</b><span>OR</span><span>AND</span><span>XNOR</span></div><div class="connector">↓ <span>index</span></div><div class="table-cells">''' + ''.join('<i></i>' for _ in range(16)) + '''</div><p class="mono">PREDICTION TABLE</p></div>'''
    if id == 'xv6':
        return '''<div class="os-diagram" role="img" aria-label="System calls connect a user program to the kernel's scheduler, memory, and threads."><div class="os-user mono">USER PROGRAM</div><div class="connector">↓ <span>system call</span></div><div class="os-kernel"><span class="mono">KERNEL</span><div><b>Scheduler</b><b>Memory</b><b>Threads</b></div></div><div class="os-base mono">RISC-V · QEMU</div></div>'''
    return '''<div class="board-diagram" role="img" aria-label="A button interrupt updates state; the main loop handles output."><span class="board-chip mono">ZYNQ</span><div class="board-flow"><span>Button</span><b>IRQ</b><span>State</span></div><div class="board-wire"></div><div class="board-flow bottom"><span>LED / LCD</span><b>Output</b><span>Main loop</span></div></div>'''


page = head('Hojoon Lee', 'Electrical and electronic engineering student at Yonsei University. Projects in operating systems, computer architecture, and embedded systems.') + header()
page += '''<main id="main">
<section class="intro wrap" id="home">
<h1>Hi, I'm Hojoon.</h1>
<p>I study electrical and electronic engineering at Yonsei University. I'm interested in operating systems, computer architecture, and memory systems.</p>
''' + link('GitHub', 'https://github.com/JOON0512', 'intro-link') + '''
</section>
<section id="work" class="section wrap"><h2>Projects</h2><div class="project-list">
'''
for p in projects:
    page += f'''<article class="project-row" id="project-{p['id']}">
<div class="project-label"><h3><a href="work/{p['id']}.html">{p['name']}</a></h3><p class="project-meta">{p['scope']}</p></div>
<div class="project-copy"><p>{p['summary']}</p><div class="project-links"><a href="work/{p['id']}.html">Notes <span aria-hidden="true">↗</span></a>'''
    if p['links']:
        page += link('Code', p['links'][0][1])
    page += '</div></div></article>\n'
page += '''</div></section>
<section id="teaching" class="section wrap"><h2>Teaching</h2>
<div class="teaching-entries">
<article><div><h3>Operating systems</h3><p class="project-meta">Tutor · Yonsei University</p></div><p>Tutored students through the department's honor society, drawing on my experience with the xv6 labs.</p></article>
<article><div><h3>Analog circuits</h3><p class="project-meta">Tutor · Spring 2025</p></div><p>Helped students with circuit theory, PSpice, and lab reports.</p></article>
<article><div><h3>CoMit</h3><p class="project-meta">Vice president · 2022–2023</p></div><p>Organized study groups and ran C programming sessions for club members.</p></article>
</div>
<div id="video-section" hidden><div id="videos" class="video-grid"></div></div>
</section>
<section id="about" class="section wrap about"><h2>About</h2><div class="about-copy">
<p>Before Yonsei, I studied industrial design and systems management engineering. I'm now finishing my undergraduate degree in electrical and electronic engineering, with graduation expected in February 2027.</p>
<p>At CORELAB, I studied ''' + link('LLVM IR through tutorials', 'https://github.com/JOON0512/LLVM101') + '''. I also learned the basics of ALD under supervision in a nanodevice lab.</p>
<p>A side project: ''' + link('History At Site', 'https://github.com/JOON0512/History_At_Site') + ''', a globe for exploring where and when films are set.</p>
</div></section>
</main>''' + footer()
(docs / 'index.html').write_text(page)

for i, p in enumerate(projects):
    following = projects[(i + 1) % len(projects)]
    page = head(p['name'] + ' — Hojoon Lee', p['intro'], '../') + header('../')
    page += f'''<main id="main" class="case wrap"><a href="../index.html#project-{p['id']}" class="back-link">← Projects</a>
<header class="case-header"><h1>{p['name']}</h1><p class="case-subtitle">{p['sub']}</p><div class="case-meta"><span>{p['scope']}</span><span>{p['tech']}</span></div></header>
<div class="case-layout"><article class="case-body"><p class="case-intro">{p['intro']}</p>'''
    for title, body in p['points']:
        page += f'<section><h2>{title}</h2><p>{body}</p></section>\n'
    page += f'''</article><aside class="case-sidebar"><figure>{visual(p['id'])}<figcaption>Schematic</figcaption></figure>'''
    if p['links']:
        page += '<div class="case-sources">' + ''.join(link(t, u, 'source-link') for t, u in p['links']) + '</div>'
    elif p.get('source_note'):
        page += f'<p class="source-note">{p["source_note"]}</p>'
    page += f'''</aside></div><a class="next-case" href="{following['id']}.html"><span>Next: {following['name']}</span><span aria-hidden="true">→</span></a></main>''' + footer('../')
    (docs / 'work' / f"{p['id']}.html").write_text(page)

(docs / 'data/projects.json').write_text(json.dumps(projects, indent=2) + '\n')
print('Built homepage and four project pages.')
