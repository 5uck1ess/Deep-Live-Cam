# --- START OF FILE globals.py ---

import os
from typing import List, Dict, Any

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKFLOW_DIR = os.path.join(ROOT_DIR, "workflow")

file_types = [
    ("Image", ("*.png", "*.jpg", "*.jpeg", "*.gif", "*.bmp", "*.webp")),
    ("Video", ("*.mp4", "*.mkv")),
]

# Face Mapping Data
source_target_map: List[Dict[str, Any]] = [] # Stores detailed map for image/video processing
simple_map: Dict[str, Any] = {}             # Stores simplified map (embeddings/faces) for live/simple mode

# Paths
source_path: str | None = None
target_path: str | None = None
output_path: str | None = None

# Processing Options
frame_processors: List[str] = []
keep_fps: bool = True
keep_audio: bool = True
keep_frames: bool = False
many_faces: bool = False         # Process all detected faces with default source
map_faces: bool = False          # Use source_target_map or simple_map for specific swaps
poisson_blend: bool = False      # Enable Poisson Blending for smoother face swaps
color_correction: bool = False   # Enable color correction (implementation specific)
nsfw_filter: bool = False

# Video Output Options
video_encoder: str | None = None
video_quality: int | None = None # Typically a CRF value or bitrate

# Live Mode Options
live_mirror: bool = False
live_resizable: bool = True
camera_input_combobox: Any | None = None # Placeholder for UI element if needed
webcam_preview_running: bool = False
show_fps: bool = False

# System Configuration
max_memory: int | None = None        # Memory limit in GB? (Needs clarification)
execution_providers: List[str] = []  # e.g., ['CUDAExecutionProvider', 'CPUExecutionProvider']
execution_threads: int | None = None # Number of threads for CPU execution
headless: bool | None = None         # Run without UI?
log_level: str = "error"             # Logging level (e.g., 'debug', 'info', 'warning', 'error')

# Face Processor UI Toggles (Example)
fp_ui: Dict[str, bool] = {"face_enhancer": False, "face_enhancer_gpen256": False, "face_enhancer_gpen512": False}

# Face Swapper Specific Options
face_swapper_enabled: bool = True # General toggle for the swapper processor
opacity: float = 1.0              # Blend factor for the swapped face (0.0-1.0)
sharpness: float = 0.0            # Sharpness enhancement for swapped face (0.0-1.0+)

# Mouth Mask Options
mouth_mask: bool = False           # Enable mouth area masking/pasting
show_mouth_mask_box: bool = False  # Visualize the mouth mask area (for debugging)
mask_feather_ratio: int = 12       # Denominator for feathering calculation (higher = smaller feather)
mask_down_size: float = 0.1        # Expansion factor for lower lip mask (relative)
mask_size: float = 1.0             # Expansion factor for upper lip mask (relative)
mouth_mask_size: float = 0.0       # Mouth mask size (0-100; 0=off, 100=mouth to chin)

# --- START: Added for Frame Interpolation ---
enable_interpolation: bool = True # Toggle temporal smoothing
interpolation_weight: float = 0  # Blend weight for current frame (0.0-1.0). Lower=smoother.
# --- END: Added for Frame Interpolation ---

# Virtual camera output (pyvirtualcam → OBS Virtual Camera driver).
# When enabled, processed frames are upscaled to VCAM 1280x720 and sent to
# the virtual cam so apps like Discord/Meet/Zoom can pick it up as a
# webcam. Requires OBS Studio installed (for the driver). Toggle is
# read at Live-start; mid-Live toggling currently requires Stop+Start.
virtual_cam: bool = False

# GFPGAN model filename. Currently shipped variants:
#   gfpgan-1024.onnx  — 512 in, 1024 out (super-res head). Highest quality.
#   gfpgan_1.4.onnx   — 512 in, 512 out. Lighter, faster.
# Hot-swap supported via reset_face_enhancer() (called from UI on change).
gfpgan_model_filename: str = "gfpgan-1024.onnx"

# Face detection resolution (160, 320, or 640).
# Lower = faster detection, fewer FLOPs, less accurate at distance.
# Changes require face analyser re-init (handled in UI by clearing FACE_ANALYSER).
det_size: int = 640

# Webcam capture resolution requested via cv2.CAP_PROP_FRAME_WIDTH/HEIGHT.
# Camera may negotiate to nearest supported size (e.g. 640x360 -> 640x480 on
# many webcams). Actual size after open is printed in console log line
# "[VideoCapturer] WxH @ FPS".
# Default 960x540 (qHD, 16:9): matches the 1280x720 vcam output ratio, so
# faces don't stretch in Discord/Meet/Zoom. 640x480 is 4:3 and looks wide
# after upscale; 360p looks low-res. 720p is camera USB-bandwidth capped
# at ~10fps on most webcams.
capture_resolution: tuple = (960, 540)

# --- END OF FILE globals.py ---

import threading
dml_lock = threading.Lock()
