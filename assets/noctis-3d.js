/* ============================================================
   NOCTIS — reusable Three.js hero scene (classic script)
   Requires THREE (r160+) on window, loaded before this file:
     <script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script>
     <script src="../assets/noctis-3d.js"></script>
   Exposes on window: mountHero, initReveals, initAnchors
   ============================================================ */
(function (global) {
  "use strict";

  // -------- Car character → scene config --------
  function CHARACTERS() {
    var T = global.THREE;
    return {
      // Rolls-Royce Spectre — slow, stately, cool chrome/silver
      spectre: {
        geometry: function () { return new T.TorusKnotGeometry(1.6, 0.48, 220, 28, 2, 3); },
        material: function () {
          return new T.MeshPhysicalMaterial({
            color: 0xc8c8cc, metalness: 1.0, roughness: 0.18,
            clearcoat: 1.0, clearcoatRoughness: 0.05, envMapIntensity: 1.2,
          });
        },
        rotationSpeed: { x: 0.08, y: 0.12 },
        keyLight: { color: 0xfff3d6, intensity: 2.2 },
        rimLight: { color: 0x88aaff, intensity: 1.1 },
      },
      // Aston Martin DB12 — warm bronze
      db12: {
        geometry: function () { return new T.TorusGeometry(1.7, 0.5, 64, 200); },
        material: function () {
          return new T.MeshPhysicalMaterial({
            color: 0x8a5a2a, metalness: 0.95, roughness: 0.22,
            clearcoat: 0.7, clearcoatRoughness: 0.15,
          });
        },
        rotationSpeed: { x: 0.05, y: 0.14 },
        keyLight: { color: 0xffd097, intensity: 2.0 },
        rimLight: { color: 0x4466aa, intensity: 0.8 },
      },
      // McLaren 750S — sharp, angular, papaya
      mclaren750s: {
        geometry: function () { return new T.IcosahedronGeometry(2.0, 0); },
        material: function () {
          return new T.MeshPhysicalMaterial({
            color: 0xee5500, metalness: 0.3, roughness: 0.28,
            clearcoat: 1.0, clearcoatRoughness: 0.08, flatShading: true,
          });
        },
        rotationSpeed: { x: 0.22, y: 0.3 },
        keyLight: { color: 0xffffff, intensity: 2.6 },
        rimLight: { color: 0xff8833, intensity: 1.3 },
      },
      // Ferrari Purosangue — rosso glossy octahedron
      purosangue: {
        geometry: function () { return new T.OctahedronGeometry(1.9, 2); },
        material: function () {
          return new T.MeshPhysicalMaterial({
            color: 0xa00010, metalness: 0.55, roughness: 0.22,
            clearcoat: 1.0, clearcoatRoughness: 0.04,
          });
        },
        rotationSpeed: { x: 0.15, y: 0.25 },
        keyLight: { color: 0xffeedd, intensity: 2.4 },
        rimLight: { color: 0xff3322, intensity: 1.2 },
      },
      // Mercedes-AMG G63 — gunmetal cube
      g63: {
        geometry: function () { return new T.BoxGeometry(2.4, 2.4, 2.4, 1, 1, 1); },
        material: function () {
          return new T.MeshPhysicalMaterial({
            color: 0x1a1d22, metalness: 0.85, roughness: 0.4,
            clearcoat: 0.5, clearcoatRoughness: 0.3,
          });
        },
        rotationSpeed: { x: 0.04, y: 0.08 },
        keyLight: { color: 0xfff0dd, intensity: 2.0 },
        rimLight: { color: 0xffaa66, intensity: 0.9 },
      },
      // Porsche 911 GT3 Touring — python green torus
      porsche911: {
        geometry: function () { return new T.TorusGeometry(1.8, 0.35, 48, 180); },
        material: function () {
          return new T.MeshPhysicalMaterial({
            color: 0xcdff55, metalness: 0.4, roughness: 0.35,
            clearcoat: 0.8, clearcoatRoughness: 0.2,
          });
        },
        rotationSpeed: { x: 0.18, y: 0.22 },
        keyLight: { color: 0xffffff, intensity: 2.2 },
        rimLight: { color: 0x4477ff, intensity: 1.0 },
      },
    };
  }

  // -------- Subtle particle backdrop --------
  function makeParticles(THREE, count) {
    count = count || 240;
    var geom = new THREE.BufferGeometry();
    var positions = new Float32Array(count * 3);
    for (var i = 0; i < count; i++) {
      var r = 8 + Math.random() * 12;
      var theta = Math.random() * Math.PI * 2;
      var phi = Math.acos(2 * Math.random() - 1);
      positions[i*3+0] = r * Math.sin(phi) * Math.cos(theta);
      positions[i*3+1] = r * Math.sin(phi) * Math.sin(theta) * 0.4;
      positions[i*3+2] = r * Math.cos(phi);
    }
    geom.setAttribute("position", new THREE.BufferAttribute(positions, 3));
    var mat = new THREE.PointsMaterial({
      color: 0xf5f1ea, size: 0.025,
      transparent: true, opacity: 0.35, sizeAttenuation: true,
    });
    return new THREE.Points(geom, mat);
  }

  // -------- Main mount function --------
  function mountHero(selector, characterKey) {
    // 3D disabled — car photos are the hero
    return;
    var el = document.querySelector(selector);
    if (!el) return;

    // Skip on reduced motion
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    // Skip on small screens (fallback image shows via CSS)
    if (window.matchMedia("(max-width: 767px)").matches) return;
    // Abort gracefully if THREE wasn't loaded
    if (!global.THREE) { console.warn("[noctis] THREE.js not loaded, skipping hero"); return; }

    var THREE = global.THREE;
    var chars = CHARACTERS();
    var config = chars[characterKey] || chars.spectre;

    var scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x0a0a0a, 0.06);

    var camera = new THREE.PerspectiveCamera(40, el.clientWidth / el.clientHeight, 0.1, 100);
    camera.position.set(0, 0.4, 7);

    var renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: "high-performance" });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setSize(el.clientWidth, el.clientHeight);
    if (THREE.ACESFilmicToneMapping !== undefined) renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.1;
    if (THREE.SRGBColorSpace !== undefined) renderer.outputColorSpace = THREE.SRGBColorSpace;
    el.appendChild(renderer.domElement);

    var geom = config.geometry();
    var mat = config.material();
    var mesh = new THREE.Mesh(geom, mat);
    scene.add(mesh);

    var particles = makeParticles(THREE);
    scene.add(particles);

    var ambient = new THREE.AmbientLight(0x332e28, 0.5);
    scene.add(ambient);

    var key = new THREE.DirectionalLight(config.keyLight.color, config.keyLight.intensity);
    key.position.set(-4, 5, 3);
    scene.add(key);

    var rim = new THREE.DirectionalLight(config.rimLight.color, config.rimLight.intensity);
    rim.position.set(4, -2, -3);
    scene.add(rim);

    var fill = new THREE.DirectionalLight(0x998866, 0.4);
    fill.position.set(2, -3, 2);
    scene.add(fill);

    // Cursor parallax
    var target = { x: 0, y: 0 };
    var current = { x: 0, y: 0 };
    function onMove(e) {
      var rect = el.getBoundingClientRect();
      var nx = ((e.clientX - rect.left) / rect.width) * 2 - 1;
      var ny = ((e.clientY - rect.top) / rect.height) * 2 - 1;
      target.x = nx * 0.25;
      target.y = ny * 0.18;
    }
    window.addEventListener("mousemove", onMove, { passive: true });

    // Resize
    var resizeT = null;
    function onResize() {
      clearTimeout(resizeT);
      resizeT = setTimeout(function () {
        var w = el.clientWidth, h = el.clientHeight;
        camera.aspect = w / h;
        camera.updateProjectionMatrix();
        renderer.setSize(w, h);
      }, 80);
    }
    window.addEventListener("resize", onResize, { passive: true });

    // Animate
    var clock = new THREE.Clock();
    var rafId;
    function tick() {
      var dt = clock.getDelta();
      current.x += (target.x - current.x) * 0.05;
      current.y += (target.y - current.y) * 0.05;

      mesh.rotation.x += dt * config.rotationSpeed.x + current.y * 0.002;
      mesh.rotation.y += dt * config.rotationSpeed.y + current.x * 0.002;
      mesh.position.y = Math.sin(clock.elapsedTime * 0.6) * 0.12;

      particles.rotation.y -= dt * 0.02;

      renderer.render(scene, camera);
      rafId = requestAnimationFrame(tick);
    }
    tick();

    window.addEventListener("pagehide", function () {
      cancelAnimationFrame(rafId);
      window.removeEventListener("mousemove", onMove);
      window.removeEventListener("resize", onResize);
      renderer.dispose(); geom.dispose(); mat.dispose();
    });
  }

  // -------- Reveal on scroll --------
  function initReveals() {
    var prefersReduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    // If the page has .reveal elements but we can't observe (old browser), show everything.
    if (!("IntersectionObserver" in window) || prefersReduce) {
      var els = document.querySelectorAll(".reveal");
      for (var i = 0; i < els.length; i++) els[i].classList.add("in-view");
      return;
    }

    // Mark the document as JS-ready so CSS can apply the hidden state safely.
    document.documentElement.classList.add("js-ready");

    var io = new IntersectionObserver(function (entries) {
      for (var i = 0; i < entries.length; i++) {
        var e = entries[i];
        if (e.isIntersecting) {
          e.target.classList.add("in-view");
          io.unobserve(e.target);
        }
      }
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });

    var reveals = document.querySelectorAll(".reveal");
    for (var j = 0; j < reveals.length; j++) io.observe(reveals[j]);
  }

  // -------- Smooth anchor scroll --------
  function initAnchors() {
    var prefersReduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var anchors = document.querySelectorAll('a[href^="#"]');
    for (var i = 0; i < anchors.length; i++) {
      anchors[i].addEventListener("click", function (e) {
        var id = this.getAttribute("href");
        if (id.length <= 1) return;
        var t = document.querySelector(id);
        if (!t) return;
        e.preventDefault();
        var y = t.getBoundingClientRect().top + window.scrollY - 72;
        window.scrollTo({ top: y, behavior: prefersReduce ? "auto" : "smooth" });
      });
    }
  }

  // Expose
  global.mountHero = mountHero;
  global.initReveals = initReveals;
  global.initAnchors = initAnchors;
})(window);
