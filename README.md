# Bali Bliss Motion Templates & Animation Library

Autonomous, self-contained 3D motion graphics templates, keyframe timelines, and animation schemas.

- **Storage Location**: [`data/bali_bliss/`](file:///Users/lashperera/Dev/Projects/bali-love-intelligence-vault/data/bali_bliss/) (or root alias [`bali_bliss/`](file:///Users/lashperera/Dev/Projects/bali-love-intelligence-vault/bali_bliss/))
- **Total Templates**: 156 fully parsed compositions
- **Total Shots**: 1,017 keyframed shots
- **Total Animated Layers**: 6,579 layers
- **Dependencies**: 100% offline JSON. Zero Supabase calls, zero external CDN links, zero video file requirements.

---

## Directory Structure

```
bali_bliss/
├── bali_bliss_motion_templates_master.json   # 22 MB unified dataset with every layer & shot embedded
├── bali_bliss_motion_catalog.json            # 68 KB index with duration, aspect ratio, shot/layer metrics
├── bali_bliss_sound_fx.json                  # 318 sound design cues & UI SFX
├── draco/                                    # Google Draco 3D WASM & JS decoders
└── templates/                                # 147 standalone individual template JSON files
    ├── vfrEUrw1.json                         # Fable Pay (9 shots, 63 layers)
    ├── qgsDf6vw.json                         # Flora AI (71 shots, 412 layers)
    ├── 2eteB61N.json                         # Framer Agent Promo (14 shots, 88 layers)
    └── ...
```

---

## Schema Architecture

Every template JSON contains the complete animation and layer hierarchy directly inside `composition`:

### 1. Template Metadata
```json
{
  "id": "ce9666de-b5e1-4c5b-b991-826933815c1b",
  "slug": "vfrEUrw1",
  "name": "Fable Pay: Finance App Launch",
  "brand": "Bali Bliss",
  "category": "product_app",
  "aspectRatio": "9:16",
  "fps": 30,
  "durationMs": 30000,
  "metrics": {
    "totalShots": 9,
    "totalLayers": 63,
    "entrancePresets": ["Rack Focus", "Slide", "Typewriter"],
    "exitPresets": ["Blur", "Focus", "Rack Focus", "Slide"]
  }
}
```

### 2. Shot & Keyframe Timeline
Each shot defines duration, transition curves, camera angles, and post-processing filters:
```json
{
  "name": "Shot 1",
  "startMs": 0,
  "duration": 3000,
  "transition": {
    "type": "fade",
    "easing": "ease-out",
    "duration": 340
  },
  "postProcessing": {
    "bloom": { "intensity": 0.4 },
    "vignette": { "darkness": 0.5 },
    "depthOfField": { "focusDistance": 0.02, "focalLength": 0.5 },
    "motionBlur": { "samples": 8 }
  }
}
```

### 3. Layer Animation (Entrance & Exit)
Each layer (text, 3D element, screen graphic, shape) defines its entrance, exit, and timing:
```json
{
  "name": "Headline",
  "kind": "text",
  "position": [0, 1.2, 0],
  "rotation": [0, 0, 0],
  "scale": [1, 1, 1],
  "inMs": 200,
  "outMs": 2800,
  "layerOrder": 2,
  "entrance": {
    "preset": "Slide Up",
    "easing": "ease-out",
    "slideX": 0,
    "slideY": -0.02,
    "blurFrom": 0,
    "scaleFrom": 1,
    "durationMs": 200,
    "stagger": { "mode": "character", "delayMs": 20 }
  },
  "exit": {
    "preset": "Rack Focus",
    "easing": "ease-in-expo",
    "blurTo": 48,
    "scaleTo": 1.08,
    "durationMs": 500
  }
}
```

---

## Offline Independence

- **Zero Cloud CDNs**: All Supabase storage links (`*.supabase.co`) have been neutralized to relative local asset paths.
- **Full Geometry & Decoders**: Includes local Draco WASM decoders (`draco_decoder.wasm`) for rendering 3D buffer geometries in Three.js / WebGL.
- **Direct Agent Consumption**: Agents can read [`bali_bliss_motion_catalog.json`](file:///Users/lashperera/Dev/Projects/bali-love-intelligence-vault/data/bali_bliss/bali_bliss_motion_catalog.json) to select templates, then load the full layer graph directly from [`templates/<slug>.json`](file:///Users/lashperera/Dev/Projects/bali-love-intelligence-vault/data/bali_bliss/templates/) without downloading external video files.
