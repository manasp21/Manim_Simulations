"""
Configuration utilities for Manim tutorials.
"""
from manim import config
import os

class TutorialConfig:
    """
    Configuration class for Manim tutorials.
    """
    
    def __init__(self, quality="medium", development=True):
        """
        Initialize configuration.
        
        Parameters
        ----------
        quality : str
            Quality setting ("low", "medium", "high", "production")
        development : bool
            Whether in development mode
        """
        self.quality = quality
        self.development = development
        self.setup_config()
    
    def setup_config(self):
        """
        Setup Manim configuration based on settings.
        """
        # Set quality
        if self.quality == "low":
            config.quality = "low_quality"
        elif self.quality == "medium":
            config.quality = "medium_quality"
        elif self.quality == "high":
            config.quality = "high_quality"
        elif self.quality == "production":
            config.quality = "production_quality"
        
        # Set development settings
        if self.development:
            config.preview = True
            config.disable_caching = True
        else:
            config.preview = False
            config.disable_caching = False
    
    def set_output_directories(self, base_dir="./"):
        """
        Set output directories.
        
        Parameters
        ----------
        base_dir : str
            Base directory for output
        """
        config.media_dir = os.path.join(base_dir, "media")
        config.video_dir = os.path.join(base_dir, "media", "videos")
        config.images_dir = os.path.join(base_dir, "media", "images")
        config.text_dir = os.path.join(base_dir, "media", "text")
    
    def set_custom_directories(self, video_dir=None, images_dir=None, text_dir=None):
        """
        Set custom output directories.
        
        Parameters
        ----------
        video_dir : str, optional
            Custom video directory
        images_dir : str, optional
            Custom images directory
        text_dir : str, optional
            Custom text directory
        """
        if video_dir:
            config.video_dir = video_dir
        if images_dir:
            config.images_dir = images_dir
        if text_dir:
            config.text_dir = text_dir

def get_tutorial_config(quality="medium", development=True):
    """
    Get a tutorial configuration instance.
    
    Parameters
    ----------
    quality : str
        Quality setting
    development : bool
        Development mode
        
    Returns
    -------
    TutorialConfig
        Configuration instance
    """
    return TutorialConfig(quality=quality, development=development)

def setup_development_config():
    """
    Setup configuration for development.
    
    Returns
    -------
    TutorialConfig
        Development configuration
    """
    config = TutorialConfig(quality="low", development=True)
    config.set_output_directories("./dev/")
    return config

def setup_production_config():
    """
    Setup configuration for production.
    
    Returns
    -------
    TutorialConfig
        Production configuration
    """
    config = TutorialConfig(quality="high", development=False)
    config.set_output_directories("./prod/")
    return config

class SceneConfig:
    """
    Configuration for individual scenes.
    """
    
    def __init__(self, scene_name, **kwargs):
        """
        Initialize scene configuration.
        
        Parameters
        ----------
        scene_name : str
            Name of the scene
        **kwargs : dict
            Additional configuration options
        """
        self.scene_name = scene_name
        self.config = kwargs
    
    def get_setting(self, key, default=None):
        """
        Get a configuration setting.
        
        Parameters
        ----------
        key : str
            Setting key
        default : any
            Default value if key not found
            
        Returns
        -------
        any
            Configuration value
        """
        return self.config.get(key, default)
    
    def set_setting(self, key, value):
        """
        Set a configuration setting.
        
        Parameters
        ----------
        key : str
            Setting key
        value : any
            Setting value
        """
        self.config[key] = value

# Default configurations
DEFAULT_DEVELOPMENT_CONFIG = {
    "quality": "low_quality",
    "preview": True,
    "disable_caching": True,
    "flush_cache": False
}

DEFAULT_PRODUCTION_CONFIG = {
    "quality": "high_quality",
    "preview": False,
    "disable_caching": False,
    "flush_cache": True
}

# Scene-specific configurations
SCENE_CONFIGURATIONS = {
    "introduction": {
        "run_time": 2.0,
        "pause_time": 1.0,
        "font_size": 36
    },
    "explanation": {
        "run_time": 1.5,
        "pause_time": 0.5,
        "font_size": 24
    },
    "demo": {
        "run_time": 1.0,
        "pause_time": 0.3,
        "font_size": 20
    },
    "conclusion": {
        "run_time": 2.5,
        "pause_time": 2.0,
        "font_size": 36
    }
}

def load_scene_config(scene_type):
    """
    Load configuration for a specific scene type.
    
    Parameters
    ----------
    scene_type : str
        Type of scene
        
    Returns
    -------
    dict
        Configuration dictionary
    """
    return SCENE_CONFIGURATIONS.get(scene_type, {})

def merge_configs(base_config, override_config):
    """
    Merge two configuration dictionaries.
    
    Parameters
    ----------
    base_config : dict
        Base configuration
    override_config : dict
        Configuration to override base
        
    Returns
    -------
    dict
        Merged configuration
    """
    merged = base_config.copy()
    merged.update(override_config)
    return merged