/**
 * ============================================================================
 * SEMESTER FINAL CODEX - APPLICATION CONTROLLER
 * Vanilla JS • Responsive Architecture • Chunked Virtualized Rendering
 * High-Performance Mobile Optimized (<1s Initial Paint at 4x CPU Throttling)
 * ============================================================================
 */

class CodexApp {
  constructor() {
    // Application State
    this.manifest = null;
    this.activeCourse = null;
    this.rawQuestions = [];
    this.filteredQuestions = [];

    // Chunked Lazy Rendering (15 cards per chunk for weak phone performance)
    this.CHUNK_SIZE = 15;
    this.renderedCount = 0;
    this.observer = null;
    this.isPrinting = false;

    // Search Engine Instance (Built lazily!)
    this.miniSearch = null;
    this.searchIndexReady = false;
    this.searchIndexPromise = null;

    // View Mode State: 'list' (sequential) or 'topic' (grouped by topic)
    this.viewMode = "list";

    // Active Filter State
    this.filters = {
      exam: "all",
      year: "2024",
      topic: "all",
      marks: "all",
      progress: "all",
      unverifiedOnly: false,
      searchQuery: ""
    };

    // Performance profiling timings
    this.profileMetrics = {};
    this.activeTermCollege = "MEC";

    // User Progress from localStorage
    this.storageKey = "du_codex_progress_v1";
    this.themeKey = "du_codex_theme_pref";
    this.userProgress = this.loadProgress();
    this.isHomeActive = true;

    // Cache DOM Elements
    this.dom = {
      appHeader: document.getElementById("appHeader"),
      activeCourseLabel: document.getElementById("activeCourseLabel"),
      searchInput: document.getElementById("searchInput"),
      clearSearchBtn: document.getElementById("clearSearchBtn"),
      themeToggleBtn: document.getElementById("themeToggleBtn"),
      courseNavbarStrip: document.getElementById("courseNavbarStrip"),
      homePortalSection: document.getElementById("homePortalSection"),
      appLayout: document.getElementById("appLayout"),
      orbitalSatellitesGroup: document.getElementById("orbitalSatellitesGroup"),
      yearScrollspyNav: document.getElementById("yearScrollspyNav"),
      mobileScrollspyBar: document.getElementById("mobileScrollspyBar"),
      resultsCountLabel: document.getElementById("resultsCountLabel"),
      questionsContainer: document.getElementById("questionsContainer"),
      scrollSentinel: document.getElementById("scrollSentinel"),
      emptyState: document.getElementById("emptyState")
    };
  }

  /**
   * Initializes Application: Theme, Event Listeners, and Data Fetching
   */
  async init() {
    this.initTheme();
    this.initMermaid();
    this.bindEvents();
    this.initObserver();
    this.bindPrintEvents();
    this.initExamSchedule();

    // Check if running from file:/// (browser sandbox blocks fetch)
    if (window.location.protocol === "file:" && !window.__CODEX_DATA__) {
      this.showFileProtocolHelp();
      return;
    }

    try {
      performance.mark("manifest-fetch-start");
      await this.fetchManifest();
      performance.mark("manifest-fetch-end");

      if (this.manifest && this.manifest.courses.length > 0) {
        this.populateCourseSelect();
        this.renderOrbitalCourses();
        const initialCourse = this.manifest.courses[0];
        await this.loadCourse(initialCourse.code);
        // Route based on URL hash or default to Home Portal
        this.handleRoute();
      }
    } catch (err) {
      console.error("Initialization error:", err);
      this.showFetchErrorHelp(err);
    }
  }

  /**
   * Guidance banner displayed when user opens via file:///
   */
  showFileProtocolHelp() {
    if (this.dom.activeCourseLabel) {
      this.dom.activeCourseLabel.innerText = "Local Server Required";
    }
    if (this.dom.resultsCountLabel) {
      this.dom.resultsCountLabel.innerText = "Local Security Sandbox Notice";
    }
    if (this.dom.emptyState) {
      this.dom.emptyState.hidden = true;
    }
    if (this.dom.topicNavbarStrip) {
      this.dom.topicNavbarStrip.innerHTML = `<span style="font-size:var(--text-xs); color:var(--accent-orange); font-weight:600; padding:4px 8px;">Notice: Browser blocked local fetch(). Run start_server.bat</span>`;
    }
    if (this.dom.questionsContainer) {
      this.dom.questionsContainer.innerHTML = `
        <div class="local-notice-card" style="
          background: var(--bg-surface-card);
          border: 1.5px solid var(--accent-primary);
          border-radius: var(--radius-md);
          padding: clamp(20px, 4vw, 36px);
          max-width: 680px;
          margin: 24px auto;
          box-shadow: 0 4px 20px rgba(0,0,0,0.06);
          text-align: left;
        ">
          <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
            <div style="width:40px; height:40px; border-radius:10px; background:rgba(30,64,175,0.1); display:flex; align-items:center; justify-content:center; color:var(--accent-primary); flex-shrink:0;" aria-hidden="true">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/>
                <path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/>
                <path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/>
                <path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/>
              </svg>
            </div>
            <div>
              <h2 style="font-size:var(--text-lg); font-weight:800; margin:0; color:var(--text-primary);">Just One Step to Launch</h2>
              <p style="font-size:var(--text-xs); color:var(--text-muted); margin:2px 0 0 0;">Browser Security Restriction (<code>file:///</code> protocol)</p>
            </div>
          </div>
          <p style="font-size:var(--text-sm); line-height:1.6; color:var(--text-secondary); margin-bottom:20px;">
            You opened <code>index.html</code> directly via <code>file:///</code>. Modern browsers (Chrome, Edge, Firefox) prohibit JavaScript <code>fetch()</code> requests on local files to prevent security sandbox vulnerabilities.
          </p>
          <div style="background:var(--bg-subtle); border-radius:var(--radius-sm); padding:16px; border-left:4px solid var(--accent-primary); margin-bottom:16px;">
            <h3 style="font-size:var(--text-sm); font-weight:700; margin:0 0 6px 0; color:var(--text-primary); display:flex; align-items:center; gap:6px;">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="color:var(--accent-primary);"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
              Method 1: 1-Click Launcher (Recommended)
            </h3>
            <p style="font-size:var(--text-xs); color:var(--text-secondary); margin:0;">
              In your project folder <code>t:\\Project\\7th Semester</code>, simply double-click <strong><code>start_server.bat</code></strong>. It automatically starts Python's local server and opens <strong>http://localhost:8000</strong> with all courses and questions loaded.
            </p>
          </div>
          <div style="background:var(--bg-subtle); border-radius:var(--radius-sm); padding:16px; border-left:4px solid var(--accent-orange); margin-bottom:16px;">
            <h3 style="font-size:var(--text-sm); font-weight:700; margin:0 0 6px 0; color:var(--text-primary); display:flex; align-items:center; gap:6px;">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="color:var(--accent-orange);"><polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/></svg>
              Method 2: Terminal
            </h3>
            <p style="font-size:var(--text-xs); color:var(--text-secondary); margin:0 0 6px 0;">Run this single command in this folder:</p>
            <code style="display:block; background:var(--bg-surface); padding:8px 12px; border-radius:4px; font-family:var(--font-mono); font-size:var(--text-xs); border:1px solid var(--border-light); color:var(--accent-primary); font-weight:600;">python -m http.server 8000</code>
            <p style="font-size:var(--text-xs); color:var(--text-secondary); margin:6px 0 0 0;">Then open <a href="http://localhost:8000" style="color:var(--accent-primary); font-weight:600; text-decoration:underline;">http://localhost:8000</a></p>
          </div>
          <div style="font-size:var(--text-xs); color:var(--text-muted); line-height:1.5; display:flex; align-items:center; gap:6px;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
            <em>When deployed to Vercel, Netlify, or GitHub Pages, it works instantly for anyone with zero setup.</em>
          </div>
        </div>
      `;
    }
  }

  showFetchErrorHelp(err) {
    if (this.dom.emptyState) this.dom.emptyState.hidden = true;
    if (this.dom.resultsCountLabel) this.dom.resultsCountLabel.innerText = "Error Loading Data";
    if (this.dom.questionsContainer) {
      this.dom.questionsContainer.innerHTML = `
        <div style="background:var(--bg-surface-card); border:1px solid var(--accent-red); border-radius:var(--radius-md); padding:24px; max-width:600px; margin:20px auto; text-align:center;">
          <h3 style="color:var(--accent-red); margin-bottom:8px; display:flex; align-items:center; justify-content:center; gap:8px;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
            Unable to load manifest data
          </h3>
          <p style="font-size:var(--text-sm); color:var(--text-secondary); margin-bottom:12px;">${err?.message || "Check if data/manifest.json exists and is valid."}</p>
          <p style="font-size:var(--text-xs); color:var(--text-muted);">If running from disk, please launch via <code>start_server.bat</code> or <code>http://localhost:8000</code>.</p>
        </div>
      `;
    }
  }

  /**
   * Safe localStorage progress handler
   */
  loadProgress() {
    try {
      const data = localStorage.getItem(this.storageKey);
      return data ? JSON.parse(data) : {};
    } catch {
      return {};
    }
  }

  saveProgress(qId, status) {
    if (this.userProgress[qId] === status) {
      delete this.userProgress[qId]; // Toggle off
    } else {
      this.userProgress[qId] = status;
    }
    try {
      localStorage.setItem(this.storageKey, JSON.stringify(this.userProgress));
    } catch (e) {
      console.warn("Storage quota exceeded", e);
    }
    this.updateProgressSummary();
  }

  /**
   * Color Theme Toggle Management
   */
  initTheme() {
    document.documentElement.setAttribute("data-theme", "light");
    try {
      localStorage.removeItem(this.themeKey);
    } catch { }
  }

  toggleTheme() {
    // Locked to light theme
    document.documentElement.setAttribute("data-theme", "light");
  }

  /**
   * Initializes Live Exam Countdown & Routine Popover
   */
  initExamSchedule() {
    const SCHEDULE = [
      { code: "CSE-4101", short: "AI", name: "Artificial Intelligence", date: new Date(2026, 10, 29, 10, 0, 0), displayDate: "29 Nov", day: "Sunday" },
      { code: "CSE-4102", short: "MSA", name: "Math & Statistical Analysis", date: new Date(2026, 11, 3, 10, 0, 0), displayDate: "03 Dec", day: "Thursday" },
      { code: "CSE-4125", short: "ML", name: "Introduction to Machine Learning", date: new Date(2026, 11, 7, 10, 0, 0), displayDate: "07 Dec", day: "Monday" },
      { code: "SS-4103", short: "ENT", name: "Entrepreneurship for IT Business", date: new Date(2026, 11, 10, 10, 0, 0), displayDate: "10 Dec", day: "Thursday" },
      { code: "CSE-4126", short: "DS", name: "Introduction to Data Science", date: new Date(2026, 11, 15, 10, 0, 0), displayDate: "15 Dec", day: "Tuesday" }
    ];

    const updateCountdown = () => {
      const now = new Date();
      let nextExam = SCHEDULE.find(e => e.date > now) || SCHEDULE[SCHEDULE.length - 1];

      const diffMs = nextExam.date - now;
      let countdownStr = "";
      if (diffMs <= 0) {
        countdownStr = "Completed";
      } else {
        const days = Math.floor(diffMs / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diffMs % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        countdownStr = days > 0 ? `${days}d ${hours}h` : `${hours}h ${Math.floor((diffMs % (1000 * 60 * 60)) / (1000 * 60))}m`;
      }

      const courseEl = document.getElementById("nextExamCourse");
      const dateEl = document.getElementById("nextExamDate");
      const countdownEl = document.getElementById("nextExamCountdown");
      if (courseEl) courseEl.innerText = nextExam.short;
      if (dateEl) dateEl.innerText = nextExam.displayDate;
      if (countdownEl) countdownEl.innerText = countdownStr;

      const listEl = document.getElementById("popoverScheduleList");
      if (listEl) {
        listEl.innerHTML = SCHEDULE.map(item => {
          const isNext = item.code === nextExam.code;
          const itemDiff = item.date - now;
          let badgeText = "";
          if (itemDiff <= 0) {
            badgeText = "Done";
          } else {
            const d = Math.floor(itemDiff / (1000 * 60 * 60 * 24));
            badgeText = isNext ? "Next Exam" : `in ${d}d`;
          }
          return `
            <div class="popover-schedule-item ${isNext ? 'is-next' : ''}" 
                 onclick="app.enterCourse('${item.code}'); document.getElementById('examSchedulePopover').hidden = true;">
              <div class="item-left">
                <div class="item-course-line">
                  <span class="item-code">${item.code}</span>
                  <span class="item-short">(${item.short})</span>
                </div>
                <span class="item-name">${item.name}</span>
              </div>
              <div class="item-right">
                <span class="item-date">${item.displayDate}</span>
                <span class="item-day">${item.day}</span>
                <span class="item-rem-badge">${badgeText}</span>
              </div>
            </div>
          `;
        }).join("");
      }
    };

    updateCountdown();
    setInterval(updateCountdown, 60000);

    const btn = document.getElementById("examCountdownBtn");
    const popover = document.getElementById("examSchedulePopover");
    if (btn && popover) {
      btn.addEventListener("click", (e) => {
        e.stopPropagation();
        popover.hidden = !popover.hidden;
      });
      document.addEventListener("click", (e) => {
        if (!popover.contains(e.target) && !btn.contains(e.target)) {
          popover.hidden = true;
        }
      });
    }
  }

  /**
   * Manifest and Course Data Loading
   */
  async fetchManifest() {
    if (window.__CODEX_DATA__ && window.__CODEX_DATA__.manifest) {
      this.manifest = window.__CODEX_DATA__.manifest;
      return;
    }
    const res = await fetch("data/manifest.json");
    if (!res.ok) throw new Error(`HTTP ${res.status} fetching manifest`);
    this.manifest = await res.json();
  }

  populateCourseSelect() {
    if (this.dom.courseSelect) {
      this.dom.courseSelect.innerHTML = this.manifest.courses
        .map(c => `<option value="${c.code}">${c.code} — ${c.name}</option>`)
        .join("");
    }
    this.renderCourseNavbar();
  }

  /**
   * Top Course Quick-Navigation Bar: Floating Centered Pill Strip (Home + 5 Courses)
   */
  renderCourseNavbar() {
    if (!this.dom.courseNavbarStrip || !this.manifest) return;

    const isHome = this.isHomeActive;

    const hubBtnHtml = `
      <button type="button" 
              class="course-nav-pill ${isHome ? 'active' : ''}" 
              title="Return to Home Hub Portal (Press [H] or [Esc])"
              onclick="app.showHomePortal()">
        <span class="nav-pill-label">Home</span>
      </button>
    `;

    const coursesHtml = this.manifest.courses.map((c, idx) => {
      const slotNum = idx + 1;
      const isActive = !isHome && this.activeCourse && this.activeCourse.code === c.code;
      const short = c.short_name || c.code.split("-")[1] || c.code;
      return `
        <button type="button" 
                class="course-nav-pill hotbar-slot ${isActive ? 'active' : ''}" 
                data-code="${c.code}"
                data-slot="${slotNum}"
                title="${c.code}: ${c.name} (Press [${slotNum}] to switch)"
                onclick="app.enterCourse('${c.code}')">
          <span class="nav-slot-key">${slotNum}</span>
          <span class="nav-pill-label">${short}</span>
        </button>
      `;
    }).join("");

    this.dom.courseNavbarStrip.innerHTML = hubBtnHtml + coursesHtml;
  }

  /**
   * Renders the 5 Courses surrounding the center Avatar in 5 cozy Bird Nests
   */
  renderOrbitalCourses() {
    if (!this.dom.orbitalSatellitesGroup || !this.manifest?.courses) return;
    const angles = [-90, -18, 54, 126, 198];
    const html = this.manifest.courses.slice(0, 5).map((c, idx) => {
      const slotNum = idx + 1;
      const angle = angles[idx] ?? (-90 + idx * 72);
      const short = c.short_name || c.code.split("-")[1] || c.code;
      return `
        <div class="orbital-satellite-node nest-satellite-node node-slot-${slotNum}"
             style="--angle: ${angle}deg;"
             onclick="app.enterCourse('${c.code}')"
             role="button"
             tabindex="0"
             aria-label="${c.code}: ${c.name}"
             title="${c.name} (${c.code}) • Press key [${slotNum}]">
          <div class="nest-wrapper">
            <img src="assets/bird_nest.png" alt="" class="nest-graphic-img">
            <div class="nest-bowl-shadow"></div>
            <div class="nest-direct-label">
              <span class="nest-slot-num">${slotNum}</span>
              <span class="nest-course-short">${short}</span>
            </div>
          </div>
        </div>
      `;
    }).join("");
    this.dom.orbitalSatellitesGroup.innerHTML = html;
  }

  /**
   * Displays the Nature Catalog Home Portal view (Navbar is completely hidden on Home page)
   */
  showHomePortal(updateHistory = true) {
    this.isHomeActive = true;
    document.body.classList.add("is-home-view");
    if (this.dom.appHeader) this.dom.appHeader.hidden = true;
    if (this.dom.homePortalSection) this.dom.homePortalSection.hidden = false;
    if (this.dom.appLayout) this.dom.appLayout.hidden = true;
    if (this.dom.activeCourseLabel) this.dom.activeCourseLabel.innerText = "DU CSE 4-1";
    document.title = "Ronaldo is the GOAT";
    this.renderCourseNavbar();
    if (updateHistory && window.location.hash && window.location.hash !== "#home" && window.location.hash !== "#") {
      history.pushState(null, "", window.location.pathname + "#home");
    }
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  /**
   * Transitions from Home Portal into the Question Feed for the chosen course (Navbar is shown)
   */
  enterCourse(courseCode, updateHistory = true) {
    this.isHomeActive = false;
    document.body.classList.remove("is-home-view");
    if (this.dom.appHeader) this.dom.appHeader.hidden = false;
    if (this.dom.homePortalSection) this.dom.homePortalSection.hidden = true;
    if (this.dom.appLayout) this.dom.appLayout.hidden = false;
    if (updateHistory) {
      const targetHash = `#${courseCode.toLowerCase()}`;
      if (window.location.hash !== targetHash) {
        history.pushState(null, "", window.location.pathname + targetHash);
      }
    }
    this.loadCourse(courseCode);
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  launchFirstCourse() {
    const firstCode = this.manifest?.courses?.[0]?.code || "CSE-4101";
    this.enterCourse(firstCode);
  }

  handleRoute() {
    const rawHash = (window.location.hash || "").replace("#", "").toLowerCase();
    const courseCodes = (this.manifest?.courses || []).map(c => c.code.toLowerCase());
    if (courseCodes.includes(rawHash)) {
      const matched = this.manifest.courses.find(c => c.code.toLowerCase() === rawHash);
      this.enterCourse(matched.code, false);
    } else {
      this.showHomePortal(false);
    }
  }

  async loadCourse(courseCode, customFile = null) {
      const course = (this.manifest?.courses || []).find(c => c.code === courseCode) || {
        code: courseCode,
        name: courseCode,
        file: customFile || `${courseCode.toLowerCase()}.json`,
        years: [2023, 2024],
        topics: []
      };

      this.activeCourse = course;
      if(this.dom.courseSelect) this.dom.courseSelect.value = course.code;
    if (this.dom.activeCourseLabel) this.dom.activeCourseLabel.innerText = "with Abokash";
    document.title = `${course.code} — Ronaldo is the GOAT`;
    this.renderCourseNavbar();

    // Default to recent year (2024) - exactly 2023 and 2024 toggles
    if (!this.filters.year || this.filters.year === "all") {
      this.filters.year = "2024";
    }
    this.filters.searchQuery = "";
    if (this.dom.searchInput) this.dom.searchInput.value = "";
    if (this.dom.clearSearchBtn) this.dom.clearSearchBtn.hidden = true;

    // Reset Search Engine
    this.miniSearch = null;
    this.searchIndexReady = false;
    this.searchIndexPromise = null;

    // Reset Scrollspy Navigation
    this.renderScrollspyNav();

    // Fetch Course Questions
    this.dom.resultsCountLabel.innerText = "Loading course questions...";

    // Performance Instrumentation
    performance.mark("load-course-start");

    try {
      if (window.__CODEX_DATA__?.courses?.[course.code] && !customFile) {
        this.rawQuestions = JSON.parse(JSON.stringify(window.__CODEX_DATA__.courses[course.code]));
      } else {
        const targetFile = customFile || (course.file.startsWith("dev/") ? course.file : `data/${course.file}`);

        performance.mark("fetch-json-start");
        const res = await fetch(targetFile);
        if (!res.ok) throw new Error(`Failed to load ${targetFile}`);
        this.rawQuestions = await res.json();
        performance.mark("fetch-json-end");
        performance.measure("time-fetch-json", "fetch-json-start", "fetch-json-end");
      }

      // Update Scrollspy Navigation
      this.renderScrollspyNav();

      // Symmetrize similar_to links across questions (fast in-memory map)
      performance.mark("relations-start");
      this.buildSymmetricRelations();
      performance.mark("relations-end");
      performance.measure("time-relations", "relations-start", "relations-end");

      // Render First-Paint Items: Both 2024 and 2023 with Left Middle Scrollspy
      performance.mark("first-paint-start");
      this.filteredQuestions = [...this.rawQuestions];
      this.renderQuestionsFeed(this.rawQuestions);
      performance.mark("first-paint-end");
      performance.measure("time-first-paint", "first-paint-start", "first-paint-end");
      performance.measure("time-total-initial-render", "load-course-start", "first-paint-end");

      // Save profiling results
      this.profileMetrics = {
        fetchAndParseJsonMs: performance.getEntriesByName("time-fetch-json")[0]?.duration || 0,
        relationsMs: performance.getEntriesByName("time-relations")[0]?.duration || 0,
        firstPaintMs: performance.getEntriesByName("time-first-paint")[0]?.duration || 0,
        totalInitialRenderMs: performance.getEntriesByName("time-total-initial-render")[0]?.duration || 0,
      };

      // DEFERRED BACKGROUND WORK:
      // 1. Build Topic Navbar in next idle frame
      if (window.requestIdleCallback) {
        requestIdleCallback(() => {
          this.renderTopicNavbar();
        });
      } else {
        setTimeout(() => {
          this.renderTopicNavbar();
        }, 50);
      }

      // 2. Schedule lazy search index generation when user is idle (or on first focus of search input)
      this.scheduleLazySearchIndex();

    } catch (err) {
      console.error(err);
      this.dom.resultsCountLabel.innerText = `Error loading questions for ${course.code}`;
    }
  }

  /**
   * Symmetrizes similar_to relationships: if A points to B, B also shows A
   */
  buildSymmetricRelations() {
    const idMap = new Map();
    const len = this.rawQuestions.length;
    for (let i = 0; i < len; i++) {
      idMap.set(this.rawQuestions[i].id, this.rawQuestions[i]);
    }

    for (let i = 0; i < len; i++) {
      const q = this.rawQuestions[i];
      if (Array.isArray(q.similar_to)) {
        const simLen = q.similar_to.length;
        for (let j = 0; j < simLen; j++) {
          const targetId = q.similar_to[j];
          const target = idMap.get(targetId);
          if (target) {
            if (!Array.isArray(target.similar_to)) target.similar_to = [];
            if (!target.similar_to.includes(q.id)) {
              target.similar_to.push(q.id);
            }
          }
        }
      }
    }
  }

  /**
   * LAZY SEARCH INDEXING (Critical for sub-second mobile render):
   * MiniSearch indexing is deferred until search box is focused or during idle time.
   */
  scheduleLazySearchIndex() {
    const buildIndex = () => {
      if (this.searchIndexReady || this.searchIndexPromise) return;

      this.searchIndexPromise = new Promise((resolve) => {
        performance.mark("search-index-start");
        if (typeof MiniSearch === "undefined") {
          this.searchIndexReady = true;
          return resolve();
        }

        this.miniSearch = new MiniSearch({
          fields: ["question", "topicsText", "solutionText"],
          storeFields: ["id"],
          searchOptions: {
            boost: { topicsText: 3, question: 2, solutionText: 1 },
            prefix: true,
            fuzzy: 0.2
          }
        });

        const documents = this.rawQuestions.map(q => ({
          id: q.id,
          question: q.question,
          topicsText: (q.topics || []).join(" "),
          solutionText: (q.solution?.steps || []).join(" ") + " " + (q.solution?.answer || "")
        }));

        this.miniSearch.addAll(documents);
        this.searchIndexReady = true;
        performance.mark("search-index-end");
        performance.measure("time-search-index", "search-index-start", "search-index-end");
        this.profileMetrics.searchIndexMs = performance.getEntriesByName("time-search-index")[0]?.duration || 0;
        resolve();
      });
    };

    // Trigger on focus of search input if present
    if (this.dom.searchInput) {
      this.dom.searchInput.addEventListener("focus", buildIndex, { once: true });
    }

    // Or trigger after 1.5 seconds when main thread is idle
    if (window.requestIdleCallback) {
      requestIdleCallback(buildIndex, { timeout: 2000 });
    } else {
      setTimeout(buildIndex, 1200);
    }
  }

  /**
   * Topic Repeat Count: Counts DISTINCT QUESTIONS that carry each topic
   * Displays as: "Appeared N times (2023, 2024)"
   */
  renderTopicFrequency() {
    const topicStats = new Map();

    // Initialize all controlled topics
    if (this.activeCourse && this.activeCourse.topics) {
      this.activeCourse.topics.forEach(t => {
        topicStats.set(t, { count: 0, years: new Set() });
      });
    }

    // Count distinct questions
    const qLen = this.rawQuestions.length;
    for (let i = 0; i < qLen; i++) {
      const q = this.rawQuestions[i];
      if (Array.isArray(q.topics)) {
        for (let j = 0; j < q.topics.length; j++) {
          const t = q.topics[j];
          if (!topicStats.has(t)) {
            topicStats.set(t, { count: 0, years: new Set() });
          }
          const stat = topicStats.get(t);
          stat.count += 1;
          if (q.year) stat.years.add(q.year);
        }
      }
    }

    // Sort by frequency descending
    const sorted = Array.from(topicStats.entries())
      .filter(([_, stat]) => stat.count > 0)
      .sort((a, b) => b[1].count - a[1].count);

    if (sorted.length === 0) {
      this.dom.topicFrequencyList.innerHTML = `<p style="font-size:0.8rem; color:var(--text-muted); padding:10px 0;">No topic stats available.</p>`;
      return;
    }

    this.dom.topicFrequencyList.innerHTML = sorted.map(([topic, stat]) => {
      const yearStr = Array.from(stat.years).sort().join(", ");
      return `
        <div class="topic-frequency-card" role="button" tabindex="0" onclick="app.filterByTopic('${topic.replace(/'/g, "\\'")}')">
          <div class="topic-name-wrap">
            <strong>${topic}</strong>
            <span class="topic-years-label">Appeared ${stat.count} times (${yearStr})</span>
          </div>
          <span class="topic-freq-badge">${stat.count}</span>
        </div>
      `;
    }).join("");
  }

  /**
   * Topic-Wise Horizontal Navbar Renderer
   * Shows every topic for the course with distinct question count badge
   */
  renderTopicNavbar() {
    if (!this.dom.topicNavbarStrip) return;

    const topicStats = new Map();
    (this.activeCourse?.topics || []).forEach(t => {
      topicStats.set(t, 0);
    });

    this.rawQuestions.forEach(q => {
      (q.topics || []).forEach(t => {
        topicStats.set(t, (topicStats.get(t) || 0) + 1);
      });
    });

    let html = `
      <button type="button" class="topic-nav-btn ${this.filters.topic === 'all' ? 'active' : ''}" 
              onclick="app.selectNavbarTopic('all')">
        <span>All Topics</span>
        <span class="topic-nav-badge">${this.rawQuestions.length}</span>
      </button>
    `;

    Array.from(topicStats.entries())
      .filter(([_, count]) => count > 0)
      .forEach(([topic, count]) => {
        const isActive = this.filters.topic === topic;
        html += `
          <button type="button" class="topic-nav-btn ${isActive ? 'active' : ''}" 
                  data-topic="${topic}"
                  onclick="app.selectNavbarTopic('${topic.replace(/'/g, "\\'")}')">
            <span>${topic}</span>
            <span class="topic-nav-badge">${count}</span>
          </button>
        `;
      });

    this.dom.topicNavbarStrip.innerHTML = html;
  }

  selectNavbarTopic(topic) {
    this.filters.topic = topic;
    if (this.dom.topicSelect) this.dom.topicSelect.value = topic;
    this.renderTopicNavbar();

    if (this.viewMode === "topic" && topic !== "all") {
      this.applyFilters();
      const slug = topic.toLowerCase().replace(/[^a-z0-9]+/g, "-");
      const targetSec = document.getElementById(`topic-sec-${slug}`);
      if (targetSec) {
        targetSec.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    } else {
      this.applyFilters();
    }
  }

  setViewMode(mode) {
    if (this.viewMode === mode) return;
    this.viewMode = mode;
    this.dom.viewModeListBtn.classList.toggle("active", mode === "list");
    this.dom.viewModeTopicBtn.classList.toggle("active", mode === "topic");
    this.applyFilters();
  }

  filterByTopic(topic) {
    this.filters.topic = topic;
    this.dom.topicSelect.value = topic;
    this.applyFilters();
  }

  /**
   * Left Rail Scrollspy Navigation Renderer (Middle of Screen)
   * Order: 2023 Final, 2024 Final, Term Test (with MEC, FEC, NITER, ShEC, SIMT)
   */
  renderScrollspyNav() {
    if (!this.dom.yearScrollspyNav) return;

    // 1. Final Exam Years (Chronological: 2023 first, then 2024)
    const years = [2023, 2024];
    const navHtml = years.map((yr, idx) => {
      const yrQuestions = this.rawQuestions.filter(q => q.year == yr && q.exam !== 'term' && !String(q.qno || '').toUpperCase().includes('TERM'));
      const isActive = idx === 0;

      const qNodes = yrQuestions.map(q => {
        const shortQ = q.qno.replace(/Question\s*/i, "Q");
        return `<button type="button" class="scrollspy-thread-node scrollspy-q-dot" data-qid="${q.id}" onclick="event.stopPropagation(); app.scrollToQuestion('${q.id}')" title="${q.qno}">${shortQ}</button>`;
      }).join("");

      return `
        <div class="scrollspy-item ${isActive ? 'active' : ''}" data-year="${yr}" onclick="app.scrollToYear('${yr}')">
          <div class="scrollspy-link">
            <span class="scrollspy-indicator-line"></span>
            <span class="scrollspy-label">${yr} FINAL</span>
          </div>
          <div class="scrollspy-thread" aria-label="${yr} Final Questions">
            ${qNodes}
          </div>
        </div>
      `;
    }).join("");

    // 2. Term Test Section (Sub-options: MEC, FEC, NITER, ShEC, SIMT)
    const colleges = ["MEC", "FEC", "NITER", "ShEC", "SIMT"];
    const collegeNodes = colleges.map(col => {
      const isColActive = this.activeTermCollege === col;
      
      const colTermTests = isColActive
        ? this.rawQuestions.filter(q => q.exam === 'term' && (q.college === col || (!q.college && col === 'MEC')))
        : [];
      
      const subNodesHtml = colTermTests.map(tt => {
        const num = String(tt.term_no || 1).padStart(2, "0");
        return `<button type="button" class="scrollspy-thread-node scrollspy-sub-tt-node scrollspy-q-dot" data-qid="${tt.id}" onclick="event.stopPropagation(); app.scrollToQuestion('${tt.id}')" title="${tt.qno}">Term Test ${num}</button>`;
      }).join("");

      return `
        <div class="college-node-group">
          <button type="button" class="scrollspy-thread-node college-thread-node college-dot ${isColActive ? 'active-college' : ''}" data-college="${col}" onclick="event.stopPropagation(); app.selectTermTestCollege('${col}')">${col}</button>
          ${subNodesHtml ? `<div class="college-subthread">${subNodesHtml}</div>` : ''}
        </div>
      `;
    }).join("");

    const termTestHtml = `
      <div class="scrollspy-item" data-year="term-test" onclick="app.scrollToSection('term-test')">
        <div class="scrollspy-link">
          <span class="scrollspy-indicator-line"></span>
          <span class="scrollspy-label">TERM TEST</span>
        </div>
        <div class="scrollspy-thread" aria-label="Term Test Engineering Colleges">
          ${collegeNodes}
        </div>
      </div>
    `;

    this.dom.yearScrollspyNav.innerHTML = navHtml + termTestHtml;

    // Mobile scrollspy bar (<900px)
    if (this.dom.mobileScrollspyBar) {
      const mobileHtml = years.map((yr, idx) => {
        const isActive = idx === 0;
        return `
          <button type="button" class="mobile-scrollspy-item ${isActive ? 'active' : ''}" data-year="${yr}" onclick="app.scrollToYear('${yr}')">
            <span class="scrollspy-indicator-line"></span>
            <span class="scrollspy-label">${yr} FINAL</span>
          </button>
        `;
      }).join("");

      const mobileTermHtml = `
        <button type="button" class="mobile-scrollspy-item" data-year="term-test" onclick="app.scrollToSection('term-test')">
          <span class="scrollspy-indicator-line"></span>
          <span class="scrollspy-label">TERM TEST</span>
        </button>
      `;

      this.dom.mobileScrollspyBar.innerHTML = mobileHtml + mobileTermHtml;
    }
  }

  /**
   * Renders All Question Sets grouped by 2023, 2024, and Term Test in the main feed
   */
  renderQuestionsFeed(questions) {
    const container = this.dom.questionsContainer;
    if (!container) return;
    container.innerHTML = "";
    if (this.dom.scrollSentinel) {
      this.dom.scrollSentinel.style.display = "none";
    }

    const list = Array.isArray(questions) ? questions : this.rawQuestions;
    this.renderedCount = list.length;
    const years = [2023, 2024]; // 2023 first, then 2024
    let totalRendered = 0;

    years.forEach(yr => {
      const yrQuestions = list.filter(q => q.year == yr && q.exam !== 'term' && !String(q.qno || '').toUpperCase().includes('TERM'));
      if (yrQuestions.length === 0) return;

      const section = document.createElement("section");
      section.className = "year-section-wrapper";
      section.id = `year-section-${yr}`;
      section.dataset.year = yr;

      section.innerHTML = `
        <div class="year-section-divider">
          <span class="year-badge-lg">${yr} FINAL EXAMINATION</span>
          <span class="year-section-sub">${yrQuestions.length} Question Sets • Answer any 5</span>
        </div>
        <div class="year-cards-list" id="cards-list-${yr}"></div>
      `;

      const cardsContainer = section.querySelector(`#cards-list-${yr}`);
      yrQuestions.forEach(q => {
        const card = this.createQuestionCard(q);
        cardsContainer.appendChild(card);
        totalRendered++;
      });

      container.appendChild(section);
    });

    // 3. Append Term Test Section
    const termSection = document.createElement("section");
    termSection.className = "year-section-wrapper term-test-section";
    termSection.id = "year-section-term-test";
    termSection.dataset.year = "term-test";

    const currentCollege = this.activeTermCollege || "MEC";

    termSection.innerHTML = `
      <div class="year-section-divider">
        <span class="year-badge-lg">TERM TEST &amp; MIDTERM PAPERS</span>
        <span class="year-section-sub">Affiliated Engineering Colleges</span>
      </div>
      <div class="term-test-college-pills-bar">
        <button type="button" class="term-college-pill ${currentCollege === 'MEC' ? 'active' : ''}" onclick="app.selectTermTestCollege('MEC')">MEC</button>
        <button type="button" class="term-college-pill ${currentCollege === 'FEC' ? 'active' : ''}" onclick="app.selectTermTestCollege('FEC')">FEC</button>
        <button type="button" class="term-college-pill ${currentCollege === 'NITER' ? 'active' : ''}" onclick="app.selectTermTestCollege('NITER')">NITER</button>
        <button type="button" class="term-college-pill ${currentCollege === 'ShEC' ? 'active' : ''}" onclick="app.selectTermTestCollege('ShEC')">ShEC</button>
        <button type="button" class="term-college-pill ${currentCollege === 'SIMT' ? 'active' : ''}" onclick="app.selectTermTestCollege('SIMT')">SIMT</button>
      </div>
      <div id="termTestCardsContainer" class="term-test-cards-wrapper"></div>
    `;

    container.appendChild(termSection);
    this.renderTermTestCards(currentCollege);

    if (this.dom.emptyState) {
      this.dom.emptyState.hidden = totalRendered > 0;
    }

    if (this.dom.resultsCountLabel) {
      this.dom.resultsCountLabel.innerHTML = "";
    }

    // Render KaTeX and Diagrams
    container.querySelectorAll(".question-set-card").forEach(card => {
      if (card.innerHTML.includes("$") || card.innerHTML.includes("\\(") || card.innerHTML.includes("\\[")) {
        this.renderMathOnContainer(card);
      }
      if (card.querySelector(".mermaid-raw-source")) {
        this.renderDiagramsOnContainer(card);
      }
    });

    // Update Scrollspy
    this.renderScrollspyNav();
    this.initScrollspy();
  }

  /**
   * Initializes IntersectionObserver for bidirectional Scrollspy
   */
  initScrollspy() {
    if (this.scrollspyObserver) {
      this.scrollspyObserver.disconnect();
    }
    if (this.qCardObserver) {
      this.qCardObserver.disconnect();
    }

    const sections = document.querySelectorAll(".year-section-wrapper");
    if (sections.length === 0) return;

    this.scrollspyObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const yr = entry.target.dataset.year;
          this.setActiveScrollspyYear(yr);
        }
      });
    }, {
      rootMargin: "-15% 0px -55% 0px",
      threshold: 0
    });

    sections.forEach(sec => this.scrollspyObserver.observe(sec));

    // Question card observer to highlight active Q dot in left nav
    const cards = document.querySelectorAll(".question-set-card");
    this.qCardObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const qId = entry.target.dataset.id;
          document.querySelectorAll(".scrollspy-q-dot").forEach(dot => {
            dot.classList.toggle("active-q", dot.dataset.qid === qId);
          });
        }
      });
    }, {
      rootMargin: "-25% 0px -50% 0px",
      threshold: 0
    });

    cards.forEach(c => this.qCardObserver.observe(c));
  }

  setActiveScrollspyYear(year) {
    document.querySelectorAll(".scrollspy-item").forEach(item => {
      const isActive = item.dataset.year == year;
      item.classList.toggle("active", isActive);
    });

    document.querySelectorAll(".mobile-scrollspy-item").forEach(item => {
      const isActive = item.dataset.year == year;
      item.classList.toggle("active", isActive);
    });
  }

  renderTermTestCards(college) {
    const container = document.getElementById("termTestCardsContainer");
    if (!container) return;
    container.innerHTML = "";

    const list = this.rawQuestions || [];
    const termQuestions = list.filter(q => q.exam === "term" && (q.college === college || (!q.college && college === "MEC")));
    const courseTitle = this.activeCourse ? `${this.activeCourse.code}: ${this.activeCourse.name}` : "Core Course";

    if (termQuestions.length > 0) {
      const listEl = document.createElement("div");
      listEl.className = "year-cards-list term-cards-list";
      termQuestions.forEach(q => {
        const card = this.createQuestionCard(q);
        listEl.appendChild(card);
      });
      container.appendChild(listEl);

      // Render math and diagrams on newly injected cards
      listEl.querySelectorAll(".question-set-card").forEach(card => {
        if (card.innerHTML.includes("$") || card.innerHTML.includes("\\(") || card.innerHTML.includes("\\[")) {
          this.renderMathOnContainer(card);
        }
        if (card.querySelector(".mermaid-raw-source")) {
          this.renderDiagramsOnContainer(card);
        }
      });

      // Re-observe cards for scrollspy active-q indicator
      if (this.qCardObserver) {
        listEl.querySelectorAll(".question-set-card").forEach(card => {
          this.qCardObserver.observe(card);
        });
      }
    } else {
      container.innerHTML = `
        <div class="term-test-placeholder-card">
          <div style="width:48px; height:48px; border-radius:12px; background:rgba(16,69,53,0.08); display:flex; align-items:center; justify-content:center; margin:0 auto 12px auto; color:#104535;" aria-hidden="true">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/>
              <rect x="8" y="2" width="8" height="4" rx="1" ry="1"/>
              <path d="M9 12h6"/>
              <path d="M9 16h6"/>
            </svg>
          </div>
          <h3 id="termTestHeading" style="margin:0 0 8px 0; font-size:var(--text-base); color:var(--text-primary); font-weight:800;">
            ${college} Term Test Examination
          </h3>
          <p style="margin:0 0 12px 0; font-size:var(--text-sm); color:var(--text-muted); line-height:1.6; max-width:620px; margin-left:auto; margin-right:auto;">
            Term Test questions for <strong>${courseTitle}</strong> for <em>${college}</em> will be added here.
          </p>
          <span style="display:inline-flex; align-items:center; gap:6px; font-size:var(--text-xs); font-weight:700; color:#104535; background:rgba(16,69,53,0.08); padding:5px 14px; border-radius:var(--radius-pill);">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
            Questions Ready for Upload
          </span>
        </div>
      `;
    }
  }

  selectTermTestCollege(college) {
    this.activeTermCollege = college;

    // Re-render left rail scrollspy navigation so the active college's subthread expands
    this.renderScrollspyNav();
    document.querySelectorAll(".scrollspy-item").forEach(item => {
      item.classList.toggle("active", item.dataset.year === "term-test");
    });

    // Update main section pills
    document.querySelectorAll(".term-college-pill").forEach(pill => {
      pill.classList.toggle("active", pill.innerText.trim() === college);
    });

    this.renderTermTestCards(college);
    this.scrollToSection("term-test");
  }

  scrollToSection(sectionId) {
    const sec = document.getElementById(`year-section-${sectionId}`);
    if (sec) {
      const yOffset = -85;
      const y = sec.getBoundingClientRect().top + window.pageYOffset + yOffset;
      window.scrollTo({ top: y, behavior: "smooth" });
      this.setActiveScrollspyYear(sectionId);
    }
  }

  scrollToYear(year) {
    this.scrollToSection(year);
  }

  scrollToQuestion(qId) {
    const card = document.getElementById(`card-${qId}`);
    if (card) {
      const yOffset = -90;
      const y = card.getBoundingClientRect().top + window.pageYOffset + yOffset;
      window.scrollTo({ top: y, behavior: "smooth" });
      card.classList.add("highlight-target");
      setTimeout(() => card.classList.remove("highlight-target"), 2500);
    }
  }

  async applyFilters() {
    let result = [...this.rawQuestions];
    const q = this.filters.searchQuery.trim();

    if (q) {
      if (!this.searchIndexReady && this.searchIndexPromise) {
        await this.searchIndexPromise;
      }

      if (this.miniSearch && this.searchIndexReady) {
        const searchResults = this.miniSearch.search(q);
        const matchingIds = new Set(searchResults.map(r => r.id));
        result = result.filter(item => matchingIds.has(item.id));
      } else {
        const lower = q.toLowerCase();
        result = result.filter(item =>
          item.question.toLowerCase().includes(lower) ||
          item.qno.toLowerCase().includes(lower) ||
          (item.subparts || []).some(sub => sub.question.toLowerCase().includes(lower))
        );
      }
    }

    this.filteredQuestions = result;
    this.renderQuestionsFeed(result);
  }

  /**
   * Topic-Grouped View Renderer
   * Organizes all questions under clear, distinct topic section headers
   */
  renderGroupedByTopic() {
    this.dom.scrollSentinel.style.display = "none";
    const container = this.dom.questionsContainer;
    container.innerHTML = "";

    if (this.filteredQuestions.length === 0) return;

    // Build map of Topic -> Questions
    const groups = new Map();
    this.filteredQuestions.forEach(q => {
      const primaryTopic = q.topics?.[0] || "General";
      if (!groups.has(primaryTopic)) groups.set(primaryTopic, []);
      groups.get(primaryTopic).push(q);
    });

    const createdCards = [];

    groups.forEach((qList, topic) => {
      const slug = topic.toLowerCase().replace(/[^a-z0-9]+/g, "-");
      const yearsSet = new Set(qList.map(q => q.year).filter(Boolean));
      const yearStr = Array.from(yearsSet).sort().join(", ");

      const section = document.createElement("section");
      section.className = "topic-group-section";
      section.id = `topic-sec-${slug}`;

      section.innerHTML = `
        <div class="topic-group-header">
          <h3 class="topic-group-title">${topic}</h3>
          <span class="topic-group-meta">Appeared ${qList.length} time${qList.length === 1 ? '' : 's'} (${yearStr})</span>
        </div>
        <div class="topic-group-cards" style="display:flex; flex-direction:column; gap:16px;"></div>
      `;

      const cardsContainer = section.querySelector(".topic-group-cards");
      qList.forEach(q => {
        const card = this.createQuestionCard(q);
        cardsContainer.appendChild(card);
        createdCards.push(card);
      });

      container.appendChild(section);
    });

    // Render KaTeX strictly on cards containing formulas
    createdCards.forEach(card => {
      if (card.innerHTML.includes("$") || card.innerHTML.includes("\\(") || card.innerHTML.includes("\\[")) {
        this.renderMathOnContainer(card);
      }
    });
  }

  /**
   * Chunked Infinite Scroll: Disabled in structured Year-Section view
   */
  renderNextChunk() {
    // All questions are rendered directly inside structured Year sections (2023, 2024, Term Test)
    if (this.dom.scrollSentinel) {
      this.dom.scrollSentinel.style.display = "none";
    }
    return;
  }

  /**
   * Renders KaTeX math strictly where formulas exist
   */
  renderMathOnContainer(element) {
    if (window.renderMathInElement) {
      try {
        window.renderMathInElement(element, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "$", right: "$", display: false },
            { left: "\\[", right: "\\]", display: true },
            { left: "\\(", right: "\\)", display: false }
          ],
          throwOnError: false
        });
      } catch (e) {
        console.warn("KaTeX error", e);
      }
    }
  }

  /**
   * Initializes Mermaid with custom Forest Green theme matching site aesthetics
   */
  initMermaid() {
    if (!window.mermaid) return;
    try {
      window.mermaid.initialize({
        startOnLoad: false,
        theme: "base",
        themeVariables: {
          darkMode: false,
          background: "#FFFFFF",
          primaryColor: "#F4F8F5",
          primaryTextColor: "#104535",
          primaryBorderColor: "#104535",
          lineColor: "#104535",
          secondaryColor: "#FEF3C7",
          tertiaryColor: "#DCFCE7",
          fontSize: "14px",
          fontFamily: "'Product Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
          edgeLabelBackground: "#FFFFFF"
        },
        flowchart: {
          curve: "basis",
          htmlLabels: true
        },
        securityLevel: "loose"
      });
    } catch (e) {
      console.warn("Mermaid init error:", e);
    }
  }

  /**
   * Enhances Mermaid code with high-contrast Forest Green node and edge color styling
   */
  enhanceMermaidCode(rawCode) {
    let code = rawCode.trim();
    if ((code.startsWith("graph TD") || code.startsWith("graph LR") || code.startsWith("flowchart TD")) && !code.includes("classDef")) {
      const styleDef = `
    classDef default fill:#F4F8F5,stroke:#104535,stroke-width:2px,color:#104535,font-weight:bold;
    classDef goal fill:#DCFCE7,stroke:#104535,stroke-width:2.5px,color:#064E3B,font-weight:bold;
    classDef start fill:#FEF3C7,stroke:#104535,stroke-width:2.5px,color:#78350F,font-weight:bold;
    classDef minNode fill:#FEF9C3,stroke:#A16207,stroke-width:2px,color:#713F12;
    classDef maxNode fill:#ECFDF5,stroke:#104535,stroke-width:2px,color:#064E3B;
    classDef leafNode fill:#FFFFFF,stroke:#104535,stroke-width:1.5px,color:#104535,font-weight:bold;
`;

      code += "\n" + styleDef;

      // Identify goal nodes
      const goalMatches = code.match(/([a-zA-Z0-9_]+)\(\([^)]*(?:Goal|Bucharest)[^)]*\)\)/gi);
      if (goalMatches) {
        goalMatches.forEach(m => {
          const id = m.split("(")[0].trim();
          code += `\n    class ${id} goal;`;
        });
      }

      // Identify start nodes (S, Root, Arad)
      if (code.includes("S((")) code += `\n    class S start;`;
      if (code.includes("Root((")) code += `\n    class Root start;`;
      if (code.includes("Arad ---")) code += `\n    class Arad start;`;

      // Identify Alpha-beta Min / Max nodes
      const minMatches = code.match(/([a-zA-Z0-9_]+)\(\([^)]*Min:[^)]*\)\)/gi);
      if (minMatches) {
        minMatches.forEach(m => {
          const id = m.split("(")[0].trim();
          code += `\n    class ${id} minNode;`;
        });
      }
      const maxMatches = code.match(/([a-zA-Z0-9_]+)\(\([^)]*Max:[^)]*\)\)/gi);
      if (maxMatches) {
        maxMatches.forEach(m => {
          const id = m.split("(")[0].trim();
          code += `\n    class ${id} maxNode;`;
        });
      }
      const leafMatches = code.match(/([a-zA-Z0-9_]+)\[[0-9]+\]/gi);
      if (leafMatches) {
        leafMatches.forEach(m => {
          const id = m.split("[")[0].trim();
          code += `\n    class ${id} leafNode;`;
        });
      }
    }
    return code;
  }

  /**
   * Renders dynamic Mermaid vector diagrams in target containers
   */
  async renderDiagramsOnContainer(container) {
    if (!container) return;
    const sources = container.querySelectorAll(".mermaid-raw-source");
    if (sources.length === 0) return;

    if (!window.mermaid) {
      for (let i = 0; i < 25; i++) {
        await new Promise(r => setTimeout(r, 100));
        if (window.mermaid) break;
      }
    }

    if (!window.mermaid) {
      sources.forEach(src => {
        const target = document.getElementById(src.dataset.targetId);
        if (target) {
          target.innerHTML = `<pre class="code-block-wrapper"><code>${src.value}</code></pre>`;
        }
      });
      return;
    }

    this.initMermaid();

    for (const src of sources) {
      const targetId = src.dataset.targetId;
      const targetEl = document.getElementById(targetId);
      if (!targetEl) continue;

      try {
        const rawCode = src.value.trim();
        const enhancedCode = this.enhanceMermaidCode(rawCode);
        const uniqueId = `mermaid-svg-${Math.random().toString(36).substr(2, 9)}`;
        const { svg } = await window.mermaid.render(uniqueId, enhancedCode);
        targetEl.innerHTML = svg;
      } catch (err) {
        console.warn("Mermaid diagram render error:", err);
        targetEl.innerHTML = `<pre class="code-block-wrapper"><code>${src.value}</code></pre>`;
      }
    }
  }

  getPracticeNotes(qId) {
    try {
      return localStorage.getItem(`du_practice_${qId}`) || "";
    } catch {
      return "";
    }
  }

  savePracticeNotes(qId, text) {
    try {
      localStorage.setItem(`du_practice_${qId}`, text);
    } catch (e) {
      console.warn("Storage quota exceeded", e);
    }
  }

  /**
   * Safe Markdown Formatter for Questions, Math, Tables, and Code
   */
  formatMarkdownText(text) {
    if (!text) return "";

    // Normalize Windows CRLF
    let out = text.replace(/\r\n/g, "\n");

    // Clean redundant '(Mermaid)' text from titles
    out = out.replace(/\s*\(Mermaid\)/gi, "");

    // 1. Extract Mermaid diagrams FIRST so diagram syntax is preserved
    const mermaidPlaceholders = [];
    out = out.replace(/```mermaid\n([\s\S]*?)```/gi, (match, code) => {
      const idx = mermaidPlaceholders.length;
      mermaidPlaceholders.push(code.trim());
      return `@@MERMAID_DIAGRAM_${idx}@@`;
    });

    // 2. Extract SVG and custom diagram HTML blocks so they are not entity-escaped
    const svgPlaceholders = [];
    out = out.replace(/<div class="svg-diagram-wrapper"[\s\S]*?<\/div>|<svg[\s\S]*?<\/svg>/gi, (match) => {
      const idx = svgPlaceholders.length;
      svgPlaceholders.push(match);
      return `@@SVG_PLACEHOLDER_${idx}@@`;
    });

    // 3. Extract Math blocks so internal '&', '\\' and newlines are not corrupted by HTML escaping or <br>
    const mathPlaceholders = [];
    // Display math ($$...$$ or \[...\])
    out = out.replace(/\$\$([\s\S]*?)\$\$|\\\[([\s\S]*?)\\\]/g, (match) => {
      const idx = mathPlaceholders.length;
      mathPlaceholders.push(match);
      return `@@MATH_PLACEHOLDER_${idx}@@`;
    });
    // Inline math ($...$ or \(...\))
    out = out.replace(/(?<!\\)\$([^\$\n]+?)(?<!\\)\$|\\\(([^\)]+?)\\\)/g, (match) => {
      const idx = mathPlaceholders.length;
      mathPlaceholders.push(match);
      return `@@MATH_PLACEHOLDER_${idx}@@`;
    });

    // 4. Escape raw HTML characters on remaining prose
    out = out
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");

    // Preserve code blocks ```lang ... ```
    out = out.replace(/```([a-z0-9_-]*)\n([\s\S]*?)```/gi, (match, lang, code) => {
      return `<pre class="code-block-wrapper"><code class="language-${lang}">${code.trim()}</code></pre>`;
    });

    // Render markdown tables
    out = out.replace(/((?:\|[^\n]+\|\n?)+)/g, (match) => {
      const rows = match.trim().split("\n");
      if (rows.length < 2) return match;
      let html = '<div class="table-scroll-wrapper"><table class="data-table">';
      rows.forEach((row, idx) => {
        if (row.includes("---")) return; // skip separator row
        const cells = row.split("|").filter((c, i, arr) => i > 0 && i < arr.length - 1);
        const tag = idx === 0 ? "th" : "td";
        html += "<tr>" + cells.map(c => `<${tag}>${c.trim()}</${tag}>`).join("") + "</tr>";
      });
      html += "</table></div>";
      return html;
    });

    // Strip standalone markdown horizontal rules ---
    out = out.replace(/^\s*---\s*$/gm, '');

    // Subpart paragraph breaks and line breaks on prose
    out = out.replace(/\n\n+/g, '<div class="set-subpart-gap"></div>');
    out = out.replace(/\n(?!\s*<)/g, '<br>');

    // Bold text **word**
    out = out.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');

    // Horizontally align adjacent Initial State and Final State tables (e.g. 8-puzzle problems)
    const puzzlePattern = /(?:<strong>\s*Initial State:?\s*<\/strong>|Initial State:?)\s*(?:<br>|\s)*<div class="table-scroll-wrapper"><table class="data-table">([\s\S]*?)<\/table><\/div>\s*(?:<div class="set-subpart-gap"><\/div>|<br>|\s)*(?:<strong>\s*Final State:?\s*<\/strong>|Final State:?)\s*(?:<br>|\s)*<div class="table-scroll-wrapper"><table class="data-table">([\s\S]*?)<\/table><\/div>/gi;
    out = out.replace(puzzlePattern, (match, table1, table2) => {
      return `
        <div class="puzzle-states-horizontal">
          <div class="puzzle-state-col">
            <span class="puzzle-state-title">Initial State:</span>
            <div class="table-scroll-wrapper"><table class="data-table">${table1}</table></div>
          </div>
          <div class="puzzle-state-arrow">&rarr;</div>
          <div class="puzzle-state-col">
            <span class="puzzle-state-title">Final State:</span>
            <div class="table-scroll-wrapper"><table class="data-table">${table2}</table></div>
          </div>
        </div>
      `;
    });

    // 5. Restore Math placeholders
    mathPlaceholders.forEach((math, idx) => {
      out = out.replace(`@@MATH_PLACEHOLDER_${idx}@@`, math);
    });

    // 6. Restore SVG / Diagram HTML placeholders
    svgPlaceholders.forEach((svg, idx) => {
      out = out.replace(`@@SVG_PLACEHOLDER_${idx}@@`, svg);
    });

    // 7. Restore Mermaid diagrams at the VERY END so newlines remain pure \n
    mermaidPlaceholders.forEach((code, idx) => {
      const diagId = `diagram-target-${Math.random().toString(36).substr(2, 9)}`;
      const replacement = `
        <div class="diagram-wrapper">
          <div class="diagram-header-label">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
            <span>Question Paper Diagram (Visual Graph)</span>
          </div>
          <div class="diagram-render-target" id="${diagId}">
            <span class="diagram-loading-indicator">Rendering visual diagram...</span>
          </div>
          <textarea class="mermaid-raw-source" data-target-id="${diagId}" style="display:none;">${code}</textarea>
        </div>
      `;
      out = out.replace(`@@MERMAID_DIAGRAM_${idx}@@`, replacement);
    });

    return out;
  }

  /**
   * Constructs DOM Node for Unified Question Set Card
   * Shows all sub-parts (a, b, c, d) and diagrams together,
   * followed by solutions with question titles above each solution.
   */
  createQuestionCard(q) {
    const card = document.createElement("article");
    card.className = "question-card question-set-card";
    card.id = `card-${q.id}`;
    card.dataset.id = q.id;

    const isUnverified = q.verified === false;

    // Subpart solutions: Each solution has its Question title above it
    let subpartsSolutionsHtml = "";
    if (Array.isArray(q.subparts) && q.subparts.length > 0) {
      subpartsSolutionsHtml = q.subparts.map(sub => {
        const subSteps = (sub.solution?.steps || [])
          .map(s => `<li>${this.formatMarkdownText(s)}</li>`)
          .join("");

        return `
          <div class="subpart-solution-block">
            <div class="subpart-solution-header">
              <span class="subpart-badge">${sub.qno}</span>
              <span class="subpart-marks">(${sub.marks} Marks)</span>
            </div>
            <div class="subpart-q-prompt">
              <span class="q-prefix">Question ${sub.qno}:</span>
              <div class="q-prompt-text">${this.formatMarkdownText(sub.question)}</div>
            </div>
            <div class="subpart-derivation">
              <strong class="solution-heading">Step-by-Step Solution:</strong>
              <ol class="solution-steps-list">${subSteps}</ol>
              ${sub.solution?.answer ? `<div class="solution-answer-box"><strong>Final Answer:</strong> ${this.formatMarkdownText(sub.solution.answer)}</div>` : ""}
              ${sub.solution?.marking_hint ? `<div class="solution-marking-hint"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg><span><strong>Marking Guide:</strong> ${this.formatMarkdownText(sub.solution.marking_hint)}</span></div>` : ""}
            </div>
          </div>
        `;
      }).join("<hr class='subpart-solution-divider'>");
    } else {
      const stepsHtml = (q.solution?.steps || [])
        .map(s => `<li>${this.formatMarkdownText(s)}</li>`)
        .join("");
      subpartsSolutionsHtml = `
        <ol class="solution-steps-list">${stepsHtml}</ol>
        <div><strong>Final Summary:</strong> ${this.formatMarkdownText(q.solution?.answer || "")}</div>
      `;
    }

    card.innerHTML = `
      <div class="card-header-row">
        <div class="card-title-group">
          <span class="q-label">${q.qno}</span>
          <span class="marks-badge">${q.marks} Marks Total</span>
          <span class="exam-year-badge">${q.exam === 'term' ? `${q.college || 'MEC'} • TERM TEST ${q.term_no || ''}` : `${q.exam.toUpperCase()} • ${q.year}`}</span>
        </div>
      </div>

      <!-- Question Set Content: All subquestions (a, b, c, d) and diagrams together -->
      <div class="q-body-text question-set-body">${this.formatMarkdownText(q.question)}</div>

      <!-- Solution Drawer for this entire Set (Hidden by default) -->
      <div class="solution-section">
        <button type="button" class="solution-toggle-btn" aria-expanded="false" onclick="app.toggleSolution('${q.id}')">
          <svg class="toggle-chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>
          <span>Reveal Solution for ${q.qno}</span>
        </button>
        <div class="solution-drawer-body" id="sol-${q.id}">
          <div class="solution-chat-bubble-container">
            <div class="chat-avatar-wrapper">
              <img src="assets/avatar_clean.png" alt="Abokash" class="chat-sender-avatar">
              <span class="chat-online-badge" title="Active now"></span>
            </div>
            <div class="chat-speech-bubble">
              <div class="chat-bubble-header">
                <span class="chat-sender-name">Abokash</span>
                <span class="chat-author-pill">Author</span>
              </div>
              <div class="chat-bubble-content">
                <p class="chat-msg-title">Solution still cooking...</p>
                <p class="chat-msg-text">In a desperate rush? Go spam Abokash's inbox.</p>
              </div>
              <div class="chat-bubble-footer">
                <a href="https://www.facebook.com/abokash89/" target="_blank" rel="noopener noreferrer" class="bother-abokash-btn" title="Send a message to Abokash on Facebook (Opens in new tab)">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                  </svg>
                  <span>Bother Abokash</span>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    `;

    return card;
  }

  toggleSolution(qId) {
    const solEl = document.getElementById(`sol-${qId}`);
    if (!solEl) return;
    const btn = solEl.previousElementSibling;
    const isOpen = solEl.classList.toggle("expanded");
    btn.setAttribute("aria-expanded", isOpen);
    btn.innerHTML = isOpen
      ? '<svg class="toggle-chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"/></svg><span>Hide Solution</span>'
      : '<svg class="toggle-chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg><span>Reveal Solution</span>';

    // Render math and diagrams inside newly opened solution drawer if needed
    if (isOpen) {
      this.renderMathOnContainer(solEl);
      this.renderDiagramsOnContainer(solEl);
    }
  }

  markProgress(qId, status) {
    this.saveProgress(qId, status);
    const card = document.getElementById(`card-${qId}`);
    if (!card) return;

    const btns = card.querySelectorAll(".prog-btn");
    btns.forEach(btn => btn.classList.remove("active"));

    const newStatus = this.userProgress[qId];
    if (newStatus) {
      const activeBtn = card.querySelector(`.prog-${newStatus.substring(0, 4)}`);
      if (activeBtn) activeBtn.classList.add("active");
    }
  }

  /**
   * Jumps to linked question from similar_to badge:
   * If target question is hidden by active filter, resets filter, renders up to target index,
   * scrolls smoothly, and applies flash highlight.
   */
  jumpToQuestion(targetId) {
    const existingCard = document.getElementById(`card-${targetId}`);
    if (existingCard) {
      existingCard.scrollIntoView({ behavior: "smooth", block: "center" });
      existingCard.classList.add("highlight-target");
      setTimeout(() => existingCard.classList.remove("highlight-target"), 2000);
      return;
    }

    // Target is either filtered out or not yet rendered in infinite scroll
    const targetIndex = this.rawQuestions.findIndex(q => q.id === targetId);
    if (targetIndex === -1) {
      alert(`Question ${targetId} not found in this course.`);
      return;
    }

    // Reset filters to reveal target
    this.resetFilters();

    // Immediately scroll to target and flash highlight
    const targetCard = document.getElementById(`card-${targetId}`);
    if (targetCard) {
      targetCard.scrollIntoView({ behavior: "smooth", block: "center" });
      targetCard.classList.add("highlight-target");
      setTimeout(() => targetCard.classList.remove("highlight-target"), 2500);
    }
  }

  /**
   * Infinite Scroll Observer Initialization (Disabled in Year-Section layout)
   */
  initObserver() {
    if (this.dom.scrollSentinel) {
      this.dom.scrollSentinel.style.display = "none";
    }
  }

  /**
   * Print View Lifecycle Hook:
   * On beforeprint, expands all solutions.
   */
  bindPrintEvents() {
    window.addEventListener("beforeprint", () => {
      this.isPrinting = true;
      // Expand all solutions
      document.querySelectorAll(".solution-drawer-body").forEach(el => {
        el.classList.add("expanded");
      });
    });

    window.addEventListener("afterprint", () => {
      this.isPrinting = false;
    });
  }

  /**
   * Updates Header Counts, Progress Bar, Empty States
   */
  updateResultsHeader() {
    const total = this.filteredQuestions.length;
    const currentYear = this.filters.year || 2024;
    if (this.dom.resultsCountLabel) {
      this.dom.resultsCountLabel.innerText = `${currentYear} Final Exam — ${total} Question Set${total === 1 ? '' : 's'} (Answer any 5)`;
    }
    if (this.dom.emptyState) {
      this.dom.emptyState.hidden = total > 0;
    }
  }

  updateProgressSummary() {
    if (this.rawQuestions.length === 0) return;
    const doneCount = this.rawQuestions.filter(q => this.userProgress[q.id] === "done").length;
    const pct = Math.round((doneCount / this.rawQuestions.length) * 100);
    this.dom.progressSummaryLabel.innerText = `Done: ${doneCount}/${this.rawQuestions.length} (${pct}%)`;
  }

  updateActiveChips() {
    let chips = [];
    if (this.filters.exam !== "all") chips.push({ label: `Exam: ${this.filters.exam}`, key: "exam" });
    if (this.filters.year !== "all") chips.push({ label: `Year: ${this.filters.year}`, key: "year" });
    if (this.filters.topic !== "all") chips.push({ label: `Topic: ${this.filters.topic}`, key: "topic" });
    if (this.filters.marks !== "all") chips.push({ label: `Marks: ${this.filters.marks}`, key: "marks" });
    if (this.filters.progress !== "all") chips.push({ label: `Status: ${this.filters.progress}`, key: "progress" });
    if (this.filters.unverifiedOnly) chips.push({ label: `Unverified Only`, key: "unverifiedOnly" });

    const count = chips.length + (this.filters.searchQuery ? 1 : 0);
    this.dom.activeFilterCount.innerText = count;
    this.dom.activeFilterCount.hidden = count === 0;
    this.dom.mobileFabCount.innerText = count;
    this.dom.mobileFabCount.hidden = count === 0;

    this.dom.activeFilterChips.innerHTML = chips.map(c => `
      <span class="filter-chip">
        ${c.label}
        <button type="button" class="chip-remove-btn" onclick="app.removeFilter('${c.key}')" aria-label="Remove filter">&times;</button>
      </span>
    `).join("");
  }

  removeFilter(key) {
    if (key === "unverifiedOnly") {
      this.filters.unverifiedOnly = false;
      this.dom.unverifiedOnlyToggle.checked = false;
    } else {
      this.filters[key] = "all";
      if (key === "topic") this.dom.topicSelect.value = "all";
      // Update pill button UI
      const groupMap = {
        exam: this.dom.examFilterGroup,
        year: this.dom.yearFilterGroup,
        marks: this.dom.marksFilterGroup,
        progress: this.dom.progressFilterGroup
      };
      if (groupMap[key]) {
        groupMap[key].querySelectorAll(".pill-btn").forEach(btn => {
          btn.classList.toggle("active", btn.dataset[key] === "all");
        });
      }
    }
    this.applyFilters();
  }

  resetFilters() {
    this.filters.exam = "all";
    this.filters.year = "all";
    this.filters.topic = "all";
    this.filters.marks = "all";
    this.filters.progress = "all";
    this.filters.unverifiedOnly = false;
    this.filters.searchQuery = "";

    if (this.dom.searchInput) this.dom.searchInput.value = "";
    if (this.dom.clearSearchBtn) this.dom.clearSearchBtn.hidden = true;
    if (this.dom.topicSelect) this.dom.topicSelect.value = "all";
    if (this.dom.unverifiedOnlyToggle) this.dom.unverifiedOnlyToggle.checked = false;

    // Reset pill button active states
    [this.dom.examFilterGroup, this.dom.yearFilterGroup, this.dom.marksFilterGroup, this.dom.progressFilterGroup].forEach(group => {
      if (!group) return;
      group.querySelectorAll(".pill-btn").forEach(btn => {
        btn.classList.toggle("active", Object.values(btn.dataset)[0] === "all");
      });
    });

    this.applyFilters();
  }

  /**
   * Event Handlers and Accessibility Listeners
   */
  bindEvents() {
    // Theme toggle
    if (this.dom.themeToggleBtn) {
      this.dom.themeToggleBtn.addEventListener("click", () => this.toggleTheme());
    }

    // Search events
    if (this.dom.searchInput) {
      this.dom.searchInput.addEventListener("input", (e) => {
        this.filters.searchQuery = e.target.value;
        if (this.dom.clearSearchBtn) this.dom.clearSearchBtn.hidden = !e.target.value;
        this.applyFilters();
      });
    }

    if (this.dom.clearSearchBtn) {
      this.dom.clearSearchBtn.addEventListener("click", () => {
        if (this.dom.searchInput) this.dom.searchInput.value = "";
        this.filters.searchQuery = "";
        this.dom.clearSearchBtn.hidden = true;
        this.applyFilters();
      });
    }

    // Hotbar keyboard shortcuts: Keys '1'..'5' to switch course, 'H' or 'Escape' for Home Hub
    window.addEventListener("keydown", (e) => {
      if (document.activeElement && ["INPUT", "TEXTAREA"].includes(document.activeElement.tagName)) return;
      if (e.key === "Escape" || e.key.toLowerCase() === "h") {
        this.showHomePortal();
        return;
      }
      const keyNum = parseInt(e.key, 10);
      if (keyNum >= 1 && keyNum <= 5 && this.manifest?.courses) {
        const targetCourse = this.manifest.courses[keyNum - 1];
        if (targetCourse) {
          e.preventDefault();
          this.enterCourse(targetCourse.code);
        }
      }
    });

    // Browser URL hash and History Routing
    window.addEventListener("hashchange", () => this.handleRoute());
    window.addEventListener("popstate", () => this.handleRoute());
  }

  setupPillGroup(groupEl, filterKey) {
    if (!groupEl) return;
    groupEl.addEventListener("click", (e) => {
      const btn = e.target.closest(".pill-btn");
      if (!btn) return;
      groupEl.querySelectorAll(".pill-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      this.filters[filterKey] = btn.dataset[filterKey];
      this.applyFilters();
    });
  }
}

// Global App Instance
const app = new CodexApp();
document.addEventListener("DOMContentLoaded", () => app.init());
