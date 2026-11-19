with open('style.css', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace font-sans with Product Sans
new_text = text.replace(
    "--font-sans: 'Inter', -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif;",
    "--font-sans: 'Product Sans', 'Google Sans', -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, sans-serif;"
)

portal_css = """
/* --------------------------------------------------------------------------
   3C. HUB NAV BUTTON IN TOP BAR
   -------------------------------------------------------------------------- */
.hub-nav-btn {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  min-height: 38px;
  padding: 6px 14px;
  border-radius: 6px;
  border: 1px solid var(--border-light);
  background: #FFFFFF;
  color: var(--text-secondary);
  font-family: var(--font-sans);
  font-size: var(--text-xs);
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.03);
  transition: all 0.15s ease;
  flex-shrink: 0;
}

.hub-nav-btn:hover {
  background-color: #F4F4F5;
  border-color: #18181B;
  color: #18181B;
}

.hub-nav-btn.active {
  background-color: #18181B;
  color: #FFFFFF;
  border-color: #18181B;
  box-shadow: 0 2px 6px rgba(24, 24, 27, 0.25);
}

.hub-nav-icon {
  display: flex;
  align-items: center;
  justify-content: center;
}

/* --------------------------------------------------------------------------
   3D. NATURE CATALOG HOME PORTAL & CIRCULAR COURSE ORBIT
   -------------------------------------------------------------------------- */
.home-portal-section {
  position: relative;
  width: 100%;
  min-height: calc(100dvh - 64px);
  background-color: #FAF8F2;
  background-image: radial-gradient(#2D4A22 1.3px, transparent 1.3px);
  background-size: 22px 22px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.home-portal-section[hidden] {
  display: none !important;
}

/* Botanical Foliage Framing */
.foliage-frame {
  position: absolute;
  pointer-events: none;
  user-select: none;
  z-index: 10;
}

.foliage-tl {
  top: 0;
  left: 0;
  width: clamp(140px, 18vw, 260px);
}

.foliage-tr {
  top: 0;
  right: 0;
  width: clamp(150px, 20vw, 280px);
}

.foliage-bottom {
  bottom: 0;
  left: 0;
  right: 0;
  width: 100%;
  max-height: clamp(110px, 18vh, 180px);
  overflow: hidden;
}

.foliage-bottom .foliage-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top center;
}

.foliage-img {
  display: block;
  width: 100%;
  height: auto;
}

/* Home Portal Center Stage */
.home-portal-stage {
  position: relative;
  z-index: 20;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  max-width: 960px;
  width: 100%;
  margin: 0 auto;
  padding: 24px 16px clamp(80px, 14vh, 140px);
}

.portal-badge-pill {
  font-family: var(--font-sans);
  font-size: 0.72rem;
  font-weight: 700;
  color: #2D4A22;
  background: rgba(45, 74, 34, 0.08);
  border: 1px solid rgba(45, 74, 34, 0.2);
  border-radius: var(--radius-pill);
  padding: 4px 14px;
  margin-bottom: 6px;
  letter-spacing: 0.04em;
}

.portal-title {
  font-family: var(--font-sans);
  font-size: clamp(1.4rem, 1.2rem + 1vw, 2.0rem);
  font-weight: 800;
  color: #1F3818;
  margin: 0 0 4px 0;
  letter-spacing: -0.02em;
}

.portal-subtitle {
  font-family: var(--font-sans);
  font-size: clamp(0.85rem, 0.8rem + 0.3vw, 0.95rem);
  color: #4B6342;
  margin-bottom: 12px;
}

/* Radial Orbital Ring System */
.orbital-ring-system {
  position: relative;
  width: clamp(340px, 78vw, 520px);
  height: clamp(340px, 78vw, 520px);
  margin: 10px auto 16px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.orbital-guide-svg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}

/* Center Avatar Core */
.portal-avatar-core {
  position: relative;
  width: clamp(110px, 18vw, 140px);
  height: clamp(110px, 18vw, 140px);
  border-radius: 50%;
  background: #FFFFFF;
  border: 3px solid #2D4A22;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  box-shadow: 0 10px 30px rgba(45, 74, 34, 0.16), inset 0 2px 4px rgba(255, 255, 255, 0.8);
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  z-index: 25;
}

.portal-avatar-core:hover {
  transform: scale(1.06);
  border-color: #F74231;
  box-shadow: 0 14px 40px rgba(247, 66, 49, 0.25);
}

.portal-core-avatar-img {
  width: auto;
  height: clamp(75px, 12vw, 98px);
  max-height: 98px;
  object-fit: contain;
  display: block;
  image-rendering: auto;
  filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.1));
}

.core-avatar-badge {
  position: absolute;
  bottom: -9px;
  background: #2D4A22;
  color: #FFFFFF;
  font-family: var(--font-sans);
  font-size: 0.65rem;
  font-weight: 800;
  padding: 2px 9px;
  border-radius: var(--radius-pill);
  letter-spacing: 0.05em;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
  transition: background 0.2s ease;
}

.portal-avatar-core:hover .core-avatar-badge {
  background: #F74231;
}

/* Orbital Satellite Nodes (Circular Course Positions) */
.orbital-satellite-node {
  position: absolute;
  top: 50%;
  left: 50%;
  --r: clamp(125px, 26vw, 195px);
  transform: translate(
    calc(-50% + cos(var(--angle)) * var(--r)),
    calc(-50% + sin(var(--angle)) * var(--r))
  );
  transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  z-index: 26;
}

.satellite-card {
  background: #FFFFFF;
  border: 1.5px solid #2D4A22;
  border-radius: 12px;
  padding: 8px 12px;
  min-width: clamp(100px, 18vw, 138px);
  max-width: 150px;
  text-align: center;
  box-shadow: 0 4px 14px rgba(45, 74, 34, 0.1);
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}

.satellite-card:hover {
  transform: scale(1.08);
  border-color: #F74231;
  box-shadow: 0 8px 24px rgba(247, 66, 49, 0.22);
}

.satellite-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 4px;
  margin-bottom: 2px;
}

.satellite-slot-badge {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  font-weight: 700;
  background: #EBF5DC;
  color: #2D4A22;
  padding: 1px 6px;
  border-radius: 4px;
}

.satellite-code-badge {
  font-family: var(--font-mono);
  font-size: 0.62rem;
  font-weight: 700;
  color: var(--text-muted);
}

.satellite-short-name {
  font-family: var(--font-sans);
  font-size: 1.05rem;
  font-weight: 800;
  color: #1F3818;
  letter-spacing: -0.01em;
  margin: 1px 0;
  transition: color 0.15s ease;
}

.satellite-card:hover .satellite-short-name {
  color: #F74231;
}

.satellite-full-title {
  font-family: var(--font-sans);
  font-size: 0.68rem;
  color: #52525B;
  line-height: 1.25;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.satellite-footer-pill {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-family: var(--font-sans);
  font-size: 0.62rem;
  font-weight: 700;
  color: #2D4A22;
  margin-top: 4px;
  transition: color 0.15s ease;
}

.satellite-card:hover .satellite-footer-pill {
  color: #F74231;
}

/* Call-to-action bar below orbit */
.portal-cta-group {
  margin-top: 6px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.portal-hint-text {
  font-family: var(--font-sans);
  font-size: 0.78rem;
  color: #4B6342;
  margin: 0;
}

.portal-hint-text kbd {
  background: #FFFFFF;
  border: 1px solid #BEDCA2;
  border-radius: 4px;
  padding: 1px 5px;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  color: #1F3818;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}

.portal-quick-btn {
  background: #2D4A22;
  color: #FFFFFF;
  border: none;
  border-radius: var(--radius-pill);
  padding: 10px 22px;
  font-family: var(--font-sans);
  font-size: 0.85rem;
  font-weight: 700;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 4px 14px rgba(45, 74, 34, 0.22);
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}

.portal-quick-btn:hover {
  background: #F74231;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(247, 66, 49, 0.35);
}
"""

idx = new_text.find('/* --------------------------------------------------------------------------\n   4. TWO-COLUMN LAYOUT')
if idx != -1:
    final_text = new_text[:idx] + portal_css + '\n' + new_text[idx:]
else:
    final_text = new_text + '\n' + portal_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(final_text)

print('Updated style.css successfully!')
