import re

with open('c:/Users/ayush/OneDrive/Desktop/sutra/sutra_3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove Testimonials HTML
exp_start = content.find('<!-- ===== REAL PEOPLE EXPERIENCE (marquee) ===== -->')
exp_end_str = '</section>\n\n<!-- ===== HOW IT WORKS (detailed flow) ===== -->'
exp_end = content.find(exp_end_str)
if exp_start != -1 and exp_end != -1:
    content = content[:exp_start] + content[exp_end + len('</section>\n\n'):]

# 2. Replace How it Works HTML
flow_start = content.find('<!-- ===== HOW IT WORKS (detailed flow) ===== -->')
flow_end_str = '<!-- ===== METHODOLOGY SECTION ===== -->'
flow_end = content.find(flow_end_str)

new_flow_html = """<!-- ===== HOW IT WORKS (Accordion flow) ===== -->
<section class="section" id="how" style="padding-top:60px;">
  <div class="wrap">
    <div class="section-head">
      <div>
        <div class="section-label">01 — The workflow</div>
        <h2 class="section-title">Five steps from a fuzzy idea to a <em>live, optimizing</em> campaign.</h2>
      </div>
      <div class="section-aside">
        Five stages, one platform. Each step feeds the next with the intelligence it needs.
      </div>
    </div>

    <div class="flow-accordion">
      <div class="flow-panel active" data-index="0">
        <div class="flow-panel-title-vertical">01. Research</div>
        <div class="flow-panel-inner">
          <div class="step-num">01</div>
          <h3><em>Consumer</em> Research</h3>
          <p class="flow-desc">AI-powered audience analysis to understand your ideal customer.</p>
          <ul class="sub-list">
            <li><b>Demographic</b>Age, gender, income, location</li>
            <li><b>Socio-economic</b>Lifestyle, employment, class</li>
            <li><b>Behavioural</b>Purchase, cultural, regional</li>
          </ul>
          <div class="output-tag">
            <span class="out-label">Output</span>
            <span class="out-val">Target audience profile</span>
          </div>
        </div>
      </div>
      
      <!-- Panel 2 -->
      <div class="flow-panel" data-index="1">
        <div class="flow-panel-title-vertical">02. Design</div>
        <div class="flow-panel-inner">
          <div class="step-num">02</div>
          <h3><em>Designing</em> Ads</h3>
          <p class="flow-desc">High-converting creative across formats — with AI or manually.</p>
          <ul class="sub-list">
            <li><b>Ad strategy</b>AI angle &amp; hook suggestions</li>
            <li><b>Script &amp; copy</b>Second-by-second direction</li>
            <li><b>Visuals &amp; video</b>Realistic actor reels, VOs</li>
          </ul>
          <div class="output-tag">
            <span class="out-label">Output</span>
            <span class="out-val">Creatives &amp; assets</span>
          </div>
        </div>
      </div>
      
      <!-- Panel 3 -->
      <div class="flow-panel" data-index="2">
        <div class="flow-panel-title-vertical">03. Playbooks</div>
        <div class="flow-panel-inner">
          <div class="step-num">03</div>
          <h3><em>Use Cases</em> Library</h3>
          <p class="flow-desc">Pre-built industry workflows so you don't start from scratch.</p>
          <ul class="sub-list">
            <li><b>Fashion</b>Photoshoots, drops, seasonals</li>
            <li><b>Real estate</b>Locality stories, walkthroughs</li>
            <li><b>+12 more</b>Gaming, D2C, edu, food, beauty</li>
          </ul>
          <div class="output-tag">
            <span class="out-label">Output</span>
            <span class="out-val">Campaign blueprints</span>
          </div>
        </div>
      </div>
      
      <!-- Panel 4 -->
      <div class="flow-panel" data-index="3">
        <div class="flow-panel-title-vertical">04. Launch</div>
        <div class="flow-panel-inner">
          <div class="step-num">04</div>
          <h3><em>Launch</em> &amp; Distribute</h3>
          <p class="flow-desc">Native integration to every channel that matters in India.</p>
          <ul class="sub-list">
            <li><b>Meta Ads</b>Facebook &amp; Instagram</li>
            <li><b>Google</b>Search, Display, YouTube</li>
            <li><b>Hotstar &amp; TikTok</b>Performance ready</li>
          </ul>
          <div class="output-tag">
            <span class="out-label">Output</span>
            <span class="out-val">Live multi-channel</span>
          </div>
        </div>
      </div>
      
      <!-- Panel 5 -->
      <div class="flow-panel" data-index="4">
        <div class="flow-panel-title-vertical">05. Optimize</div>
        <div class="flow-panel-inner">
          <div class="step-num">05</div>
          <h3><em>Optimize</em> &amp; Scale</h3>
          <p class="flow-desc">AI watches every metric and shifts spend to what wins.</p>
          <ul class="sub-list">
            <li><b>A/B testing</b>Hooks, copies, audiences</li>
            <li><b>Budget allocation</b>Auto-shifted to winners</li>
            <li><b>Retargeting</b>Behaviour-aware automation</li>
          </ul>
          <div class="output-tag">
            <span class="out-label">Output</span>
            <span class="out-val">Lower CPA, higher ROI</span>
          </div>
        </div>
      </div>

    </div>

    <!-- Continuous loop -->
    <div class="loop-strip" style="margin-top: 40px;">
      <span class="ic">∞</span>
      <span>Continuous learning loop</span>
      <span class="arr">→</span>
      <span>Data collection</span>
      <span class="arr">→</span>
      <span>AI pattern recognition</span>
      <span class="arr">→</span>
      <span>Smarter targeting next cycle</span>
    </div>
  </div>
</section>

"""

if flow_start != -1 and flow_end != -1:
    content = content[:flow_start] + new_flow_html + content[flow_end:]

# 3. Replace CSS
css_old_start = content.find('/* ===== HOW IT WORKS (detailed flow) ===== */')
css_old_end = content.find('/* ===== FEATURE PILLARS (pop out, soft animations) ===== */')

new_css = """/* ===== HOW IT WORKS (Accordion flow) ===== */
  .flow-accordion {
    display: flex;
    gap: 16px;
    height: 520px;
    margin-top: 40px;
  }
  @media (max-width: 980px) {
    .flow-accordion {
      flex-direction: column;
      height: auto;
      gap: 12px;
    }
  }
  .flow-panel {
    flex: 1;
    background: var(--paper-3);
    border: 1px solid var(--line);
    border-radius: 24px;
    position: relative;
    overflow: hidden;
    cursor: pointer;
    transition: flex 0.6s cubic-bezier(0.25, 1, 0.5, 1), background 0.4s ease, border-color 0.4s ease, box-shadow 0.4s ease;
  }
  @media (max-width: 980px) {
    .flow-panel {
      height: 80px;
      transition: height 0.6s cubic-bezier(0.25, 1, 0.5, 1), background 0.4s ease, border-color 0.4s ease;
      flex: none;
    }
    .flow-panel.active {
      height: 480px;
    }
  }
  .flow-panel:hover, .flow-panel.active {
    flex: 4;
    background: var(--paper-2);
    border-color: var(--accent-soft);
    box-shadow: 0 16px 40px rgba(138,79,85, 0.12), inset 0 0 0 1px rgba(138,79,85,0.2);
  }
  .flow-panel-title-vertical {
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%) rotate(180deg);
    writing-mode: vertical-rl;
    white-space: nowrap;
    font-family: 'Instrument Serif', serif;
    font-size: 26px;
    color: var(--ink-soft);
    transition: opacity 0.3s ease;
    letter-spacing: 0.02em;
    pointer-events: none;
  }
  @media (max-width: 980px) {
    .flow-panel-title-vertical {
      writing-mode: horizontal-tb;
      transform: translate(-50%, -50%);
      top: 40px;
      width: 100%;
      text-align: center;
    }
  }
  .flow-panel:hover .flow-panel-title-vertical, .flow-panel.active .flow-panel-title-vertical {
    opacity: 0;
  }
  .flow-panel-inner {
    width: 380px;
    height: 100%;
    padding: 40px 32px;
    opacity: 0;
    transition: opacity 0.4s ease 0.2s;
    pointer-events: none;
    display: flex;
    flex-direction: column;
  }
  @media (max-width: 980px) {
    .flow-panel-inner {
      width: 100%;
      padding: 32px 24px;
    }
  }
  .flow-panel:hover .flow-panel-inner, .flow-panel.active .flow-panel-inner {
    opacity: 1;
    pointer-events: auto;
  }
  .flow-panel-inner .step-num {
    width: 44px; height: 44px; border-radius: 50%;
    background: var(--accent); color: #fff;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Geist Mono', monospace; font-size: 14px;
    margin-bottom: 20px;
    box-shadow: 0 0 0 6px rgba(138,79,85,0.15);
  }
  .flow-panel-inner h3 {
    font-family: 'Instrument Serif', serif; font-weight: 400;
    font-size: 28px; line-height: 1.1; letter-spacing: -0.01em;
    color: var(--ink);
    margin-bottom: 8px;
  }
  .flow-panel-inner h3 em { font-style: italic; color: var(--accent); }
  .flow-panel-inner .flow-desc {
    font-size: 14px; color: var(--ink-soft); line-height: 1.5;
    margin-bottom: 24px;
  }
  .flow-panel-inner .sub-list {
    list-style: none; margin-bottom: 24px; flex-grow: 1;
  }
  .flow-panel-inner .sub-list li {
    font-size: 13px; color: var(--ink-soft);
    padding: 10px 0; border-top: 1px dashed var(--line);
    display: flex; align-items: flex-start; gap: 10px;
  }
  .flow-panel-inner .sub-list li::before {
    content: ""; width: 5px; height: 5px; border-radius: 50%;
    background: var(--accent); margin-top: 8px; flex-shrink: 0;
  }
  .flow-panel-inner .sub-list li b { color: var(--ink); font-weight: 600; display: block; }
  .flow-panel-inner .output-tag {
    background: var(--paper); color: var(--ink);
    border: 1px solid var(--line-strong);
    padding: 12px 16px; border-radius: 12px;
    font-family: 'Geist Mono', monospace; font-size: 10px;
    letter-spacing: 0.14em; text-transform: uppercase;
    text-align: center;
    margin-top: auto;
  }
  .flow-panel-inner .output-tag .out-label {
    display: block; color: var(--accent-3); font-size: 9px;
    margin-bottom: 4px; opacity: 0.8;
  }
  .flow-panel-inner .output-tag .out-val {
    color: var(--ink); font-size: 12px; font-weight: 500;
  }

  /* future extension callout */
  .future-callout{
    margin-top:24px;
    padding:24px 30px;
    border:1px dashed var(--line-strong);
    border-radius:14px;
    background:transparent;
    display:flex; align-items:center; gap:24px; flex-wrap:wrap;
  }
  .future-callout .badge{
    font-family:'Geist Mono',monospace; font-size:10px;
    letter-spacing:0.18em; text-transform:uppercase;
    color:var(--accent-3);
    padding:4px 10px; border:1px solid var(--accent-3);
    border-radius:99px;
  }
  .future-callout h5{
    font-family:'Instrument Serif',serif; font-weight:400;
    font-size:20px; flex:1; line-height:1.3;
  }
  .future-callout h5 em{ font-style:italic; color:var(--accent); }
  .future-steps{
    display:flex; gap:14px; font-family:'Geist Mono',monospace;
    font-size:10px; letter-spacing:0.14em; text-transform:uppercase;
    color:var(--ink-mute);
    align-items:center;
  }
  .future-steps span{
    padding:6px 10px; background:var(--paper-2);
    border-radius:6px; border:1px solid var(--line);
  }
  .future-steps .ar{ color:var(--accent-3); padding:0; background:none; border:none; }

  /* continuous loop */
  .loop-strip{
    margin-top:24px; text-align:center;
    padding:18px 24px;
    background:var(--paper-3); border-radius:99px;
    font-family:'Geist Mono',monospace; font-size:11px;
    letter-spacing:0.16em; text-transform:uppercase;
    color:var(--ink-soft);
    display:flex; justify-content:center; align-items:center; gap:14px; flex-wrap:wrap;
  }
  .loop-strip .ic{
    width:28px; height:28px; border-radius:50%;
    border:1.5px solid var(--accent);
    color:var(--accent);
    display:inline-flex; align-items:center; justify-content:center;
    font-family:'Instrument Serif',serif; font-style:italic; font-size:18px;
    background:var(--paper);
  }
  .loop-strip .arr{ color:var(--accent); }

  """

if css_old_start != -1 and css_old_end != -1:
    content = content[:css_old_start] + new_css + content[css_old_end:]

# 4. Remove Testimonials CSS & Old dark theme CSS
content = re.sub(r'/\* ===== REAL PEOPLE EXPERIENCE \(marquee\) ===== \*/.*?/\* ===== SECTION HEADERS ===== \*/', '/* ===== SECTION HEADERS ===== */', content, flags=re.DOTALL)
content = re.sub(r'/\* Experience marquee cards \*/.*?/\* Section header borders \*/', '/* Section header borders */', content, flags=re.DOTALL)
content = re.sub(r'/\* Flow cards \*/.*?/\* Loop strip \*/', '/* Loop strip */', content, flags=re.DOTALL)
content = re.sub(r'/\* ── FLOW ANIMATION ── \*/.*?/\* ── METHODOLOGY SECTION ── \*/', '/* ── METHODOLOGY SECTION ── */', content, flags=re.DOTALL)

# 5. Replace Javascript
js_old_start = content.find('// ── Flow card animated connectors ──')
js_old_end = content.find('// ── CIM canvas orbital animation (refined, palette-only) ──')

new_js = """// ── Accordion Interaction ──
  (function() {
    const panels = document.querySelectorAll('.flow-panel');
    if (!panels.length) return;
    let activeIndex = 0;
    let autoPlay;

    function activatePanel(index) {
      panels.forEach(p => p.classList.remove('active'));
      panels[index].classList.add('active');
      activeIndex = index;
    }

    function startAutoPlay() {
      stopAutoPlay();
      autoPlay = setInterval(() => {
        activatePanel((activeIndex + 1) % panels.length);
      }, 4000);
    }

    function stopAutoPlay() {
      if (autoPlay) clearInterval(autoPlay);
    }

    panels.forEach((panel, i) => {
      panel.addEventListener('mouseenter', () => {
        stopAutoPlay();
        activatePanel(i);
      });
      panel.addEventListener('mouseleave', () => {
        startAutoPlay();
      });
      panel.addEventListener('click', () => {
        stopAutoPlay();
        activatePanel(i);
        startAutoPlay();
      });
    });

    startAutoPlay();
  })();

  """

if js_old_start != -1 and js_old_end != -1:
    content = content[:js_old_start] + new_js + content[js_old_end:]

with open('c:/Users/ayush/OneDrive/Desktop/sutra/sutra_3.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done refactoring')
