/* =============================================
   NEXUS STUDIO CODE — Enterprise Core JavaScript
   ============================================= */

document.addEventListener('DOMContentLoaded', () => {

  // ── 1. Navbar scroll styling ──
  const nav = document.getElementById('mainNav');
  const handleScroll = () => {
    nav?.classList.toggle('scrolled', window.scrollY > 40);
  };
  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();

  // ── 2. Scroll reveal animations ──
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' });

  document.querySelectorAll('.reveal-up, .reveal-left, .reveal-right').forEach(el => {
    revealObserver.observe(el);
  });

  // ── 3. Counter animations for metrics ──
  const animateCounter = (el) => {
    const target = parseInt(el.dataset.target, 10) || 0;
    const duration = 1800;
    const step = target / (duration / 16);
    let current = 0;
    const timer = setInterval(() => {
      current = Math.min(current + step, target);
      el.textContent = Math.floor(current).toLocaleString('es-AR');
      if (current >= target) {
        clearInterval(timer);
        el.textContent = target.toLocaleString('es-AR');
      }
    }, 16);
  };

  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        counterObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.4 });

  document.querySelectorAll('.stat-number[data-target]').forEach(el => {
    counterObserver.observe(el);
  });

  // ── 4. Smooth scroll for anchor links ──
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', e => {
      const id = link.getAttribute('href');
      if (id === '#') return;
      const target = document.querySelector(id);
      if (target) {
        e.preventDefault();
        const offset = 80;
        const top = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top, behavior: 'smooth' });
        // Close mobile navbar if open
        const collapse = document.getElementById('navbarNav');
        if (collapse && collapse.classList.contains('show')) {
          const bsCollapse = bootstrap.Collapse.getInstance(collapse);
          if (bsCollapse) bsCollapse.hide();
        }
      }
    });
  });

  // ── 5. Hero IDE Code Window Tabs & Copy ──
  const codeTabButtons = document.querySelectorAll('#heroCodeTabs .code-tab-btn');
  const codeTabPanes = {
    backend: document.getElementById('code-tab-backend'),
    models: document.getElementById('code-tab-models'),
    architecture: document.getElementById('code-tab-architecture'),
  };

  codeTabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetTab = btn.dataset.tab;
      codeTabButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      Object.keys(codeTabPanes).forEach(k => {
        const pane = codeTabPanes[k];
        if (pane) {
          if (k === targetTab) {
            pane.classList.remove('d-none');
            pane.classList.add('active');
          } else {
            pane.classList.add('d-none');
            pane.classList.remove('active');
          }
        }
      });
    });
  });

  const copyCodeBtn = document.getElementById('copyCodeBtn');
  if (copyCodeBtn) {
    copyCodeBtn.addEventListener('click', () => {
      const activePane = document.querySelector('.tab-pane-code:not(.d-none) code');
      if (activePane) {
        navigator.clipboard.writeText(activePane.innerText).then(() => {
          const originalHTML = copyCodeBtn.innerHTML;
          copyCodeBtn.innerHTML = '<i class="bi bi-check2 text-success"></i>';
          setTimeout(() => {
            copyCodeBtn.innerHTML = originalHTML;
          }, 2000);
        });
      }
    });
  }

  // ── 6. Interactive Quote Calculator Engine ──
  const quoteForm = document.getElementById('quoteCalculatorForm');
  const costDisplay = document.getElementById('estimatedCostDisplay');
  const timelineDisplay = document.getElementById('estimatedTimelineDisplay');
  const hiddenCost = document.getElementById('hiddenEstimatedCost');
  const hiddenBudgetRange = document.getElementById('hiddenBudgetRange');

  if (quoteForm && costDisplay && timelineDisplay) {
    const calculateEstimate = () => {
      // 1. Base project type
      const selectedType = quoteForm.querySelector('input[name="project_type"]:checked');
      let basePrice = selectedType ? parseFloat(selectedType.dataset.basePrice) || 1800 : 1800;
      let baseWeeks = selectedType ? parseFloat(selectedType.dataset.baseWeeks) || 4 : 4;

      // 2. Additional features
      const selectedFeatures = quoteForm.querySelectorAll('input[name="features"]:checked');
      let featuresPrice = 0;
      let featuresWeeks = 0;
      selectedFeatures.forEach(feat => {
        featuresPrice += parseFloat(feat.dataset.price) || 0;
        featuresWeeks += parseFloat(feat.dataset.weeks) || 0;
      });

      // 3. Timeline multiplier
      const selectedTimeline = quoteForm.querySelector('input[name="timeline"]:checked');
      const timelineMultiplier = selectedTimeline ? parseFloat(selectedTimeline.dataset.multiplier) || 1.0 : 1.0;

      // Calculation logic
      const totalRaw = (basePrice + featuresPrice) * timelineMultiplier;
      const minEstimate = Math.round((totalRaw * 0.9) / 50) * 50;
      const maxEstimate = Math.round((totalRaw * 1.15) / 50) * 50;

      const totalWeeks = Math.max(2, Math.round((baseWeeks + featuresWeeks)));
      const minWeeks = Math.max(2, totalWeeks - 1);
      const maxWeeks = totalWeeks + 1;

      // Format displays
      const formattedCost = `USD $${minEstimate.toLocaleString('en-US')} - $${maxEstimate.toLocaleString('en-US')}`;
      const formattedTimeline = `<i class="bi bi-clock-history text-accent me-1"></i>Tiempo estimado de desarrollo: <strong>${minWeeks} a ${maxWeeks} semanas</strong>`;

      costDisplay.textContent = formattedCost;
      timelineDisplay.innerHTML = formattedTimeline;

      if (hiddenCost) hiddenCost.value = formattedCost;
      if (hiddenBudgetRange) hiddenBudgetRange.value = `${minEstimate} - ${maxEstimate} USD`;
    };

    // Listen to changes on all radios & checkboxes in quoteForm
    quoteForm.querySelectorAll('input[type="radio"], input[type="checkbox"]').forEach(input => {
      input.addEventListener('change', calculateEstimate);
    });

    // Initial calculation on page load
    calculateEstimate();

    // AJAX Form Submission
    quoteForm.addEventListener('submit', function(e) {
      // If browser validation passes, handle submit
      if (!this.checkValidity()) {
        return; // standard HTML5 validation will trigger
      }

      e.preventDefault();
      const submitBtn = document.getElementById('quoteSubmitBtn');
      const originalBtnHTML = submitBtn ? submitBtn.innerHTML : '';
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>Procesando propuesta...';
      }

      const formData = new FormData(this);

      fetch(this.action, {
        method: 'POST',
        body: formData,
        headers: {
          'X-Requested-With': 'XMLHttpRequest'
        }
      })
      .then(res => res.json())
      .then(data => {
        if (data.status === 'ok') {
          // Show interactive modal / banner or notification
          const successBox = document.createElement('div');
          successBox.className = 'alert alert-success mt-4 p-4 rounded-4 shadow-lg border-accent text-white';
          successBox.innerHTML = `
            <div class="d-flex align-items-center mb-2">
              <i class="bi bi-check-circle-fill text-accent fs-3 me-3"></i>
              <h4 class="mb-0 text-white">¡Solicitud Registrada con Éxito!</h4>
            </div>
            <p class="mb-2">${data.message}</p>
            <p class="small text-muted mb-0"><i class="bi bi-shield-check text-accent me-1"></i>ID de Consulta: #${data.quote_id} · Hemos guardado todos tus requerimientos técnicos.</p>
          `;
          quoteForm.parentNode.insertBefore(successBox, quoteForm);
          quoteForm.style.opacity = '0.5';
          quoteForm.style.pointerEvents = 'none';
          successBox.scrollIntoView({ behavior: 'smooth', block: 'center' });
        } else {
          alert(data.message || 'Ocurrió un error al enviar la solicitud. Por favor intenta nuevamente.');
          if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.innerHTML = originalBtnHTML;
          }
        }
      })
      .catch(() => {
        // Fallback to standard form submit if fetch fails
        quoteForm.submit();
      });
    });
  }

  // ── 7. Tech Stack Category Tabs in Home ──
  const techTabBtns = document.querySelectorAll('.tech-tabs-nav .tech-tab-btn');
  const techItems = document.querySelectorAll('.tech-grid .tech-item');

  if (techTabBtns.length > 0 && techItems.length > 0) {
    techTabBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const cat = btn.dataset.category;
        techTabBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        techItems.forEach(item => {
          if (cat === 'all' || item.dataset.category === cat) {
            item.style.display = 'flex';
            item.classList.add('revealed');
          } else {
            item.style.display = 'none';
          }
        });
      });
    });
  }

  // ── 8. Active Nav item highlight by scroll ──
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');
  const highlightObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        navLinks.forEach(l => l.classList.remove('active'));
        const match = document.querySelector(`.nav-link[href*="#${entry.target.id}"]`);
        match?.classList.add('active');
      }
    });
  }, { threshold: 0.35 });
  sections.forEach(s => highlightObserver.observe(s));

  // ── 9. Tilt 3D Micro-interaction on Cards ──
  document.querySelectorAll('.service-card, .case-study-card, .process-step-card, .guarantee-card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width - 0.5;
      const y = (e.clientY - rect.top) / rect.height - 0.5;
      card.style.transform = `perspective(800px) rotateY(${x * 4}deg) rotateX(${-y * 4}deg) translateY(-4px)`;
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
    });
  });

  // ── 10. Auto-dismiss Toasts ──
  document.querySelectorAll('.toast.show').forEach(t => {
    setTimeout(() => {
      const toast = bootstrap.Toast.getOrCreateInstance(t);
      if (toast) toast.hide();
    }, 6000);
  });

  console.log('%c🚀 Nexus Studio Code — Enterprise Web System Active', 'color:#00ff88;font-size:16px;font-weight:bold;');
  console.log('%cIngeniería de Software & Arquitecturas Escalables', 'color:#8be9fd;font-size:12px;');
});
