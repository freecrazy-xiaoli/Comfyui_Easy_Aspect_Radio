import torch

class AspectRatio:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
    
        aspect_ratios = ["custom",
                         "SD1.5 - 1:1 square 512x512",
                         "SD1.5 - 2:3 portrait 512x768",
                         "SD1.5 - 3:4 portrait 512x682",
                         "SD1.5 - 3:2 landscape 768x512",
                         "SD1.5 - 4:3 landscape 682x512",
                         "SD1.5 - 16:9 cinema 910x512",
                         "SD1.5 - 1.85:1 cinema 952x512",
                         "SD1.5 - 2:1 cinema 1024x512",
                         "SDXL - 1:1 square 1024x1024",
                         "SDXL - 3:4 portrait 896x1152",
                         "SDXL - 5:8 portrait 832x1216",
                         "SDXL - 9:16 portrait 768x1344",
                         "SDXL - 9:21 portrait 640x1536",
                         "SDXL - 4:3 landscape 1152x896",
                         "SDXL - 3:2 landscape 1216x832",
                         "SDXL - 16:9 landscape 1344x768",
                         "SDXL - 21:9 landscape 1536x640"]
               
        return {
            "required": {
                "width": ("INT", {"default": 1024, "min": 64, "max": 8192}),
                "height": ("INT", {"default": 1024, "min": 64, "max": 8192}),
                "aspect_ratio": (aspect_ratios,),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 64})
            }
        }
    RETURN_TYPES = ("INT", "INT",  "LATENT", "INT", )
    RETURN_NAMES = ("width", "height", "empty_latent", "batch_size", )
    FUNCTION = "Aspect_Ratio"
    CATEGORY = "image"

    def Aspect_Ratio(self, width, height, aspect_ratio, batch_size):
        
        # SD1.5
        if aspect_ratio == "SD1.5 - 1:1 square 512x512":
            width, height = 512, 512
        elif aspect_ratio == "SD1.5 - 2:3 portrait 512x768":
            width, height = 512, 768
        elif aspect_ratio == "SD1.5 - 16:9 cinema 910x512":
            width, height = 910, 512
        elif aspect_ratio == "SD1.5 - 3:4 portrait 512x682":
            width, height = 512, 682
        elif aspect_ratio == "SD1.5 - 3:2 landscape 768x512":
            width, height = 768, 512    
        elif aspect_ratio == "SD1.5 - 4:3 landscape 682x512":
            width, height = 682, 512
        elif aspect_ratio == "SD1.5 - 1.85:1 cinema 952x512":            
            width, height = 952, 512
        elif aspect_ratio == "SD1.5 - 2:1 cinema 1024x512":
            width, height = 1024, 512
        elif aspect_ratio == "SD1.5 - 2.39:1 anamorphic 1224x512":
            width, height = 1224, 512 
        # SDXL   
        if aspect_ratio == "SDXL - 1:1 square 1024x1024":
            width, height = 1024, 1024
        elif aspect_ratio == "SDXL - 3:4 portrait 896x1152":
            width, height = 896, 1152
        elif aspect_ratio == "SDXL - 5:8 portrait 832x1216":
            width, height = 832, 1216
        elif aspect_ratio == "SDXL - 9:16 portrait 768x1344":
            width, height = 768, 1344
        elif aspect_ratio == "SDXL - 9:21 portrait 640x1536":
            width, height = 640, 1536
        elif aspect_ratio == "SDXL - 4:3 landscape 1152x896":
            width, height = 1152, 896
        elif aspect_ratio == "SDXL - 3:2 landscape 1216x832":
            width, height = 1216, 832
        elif aspect_ratio == "SDXL - 16:9 landscape 1344x768":
            width, height = 1344, 768
        elif aspect_ratio == "SDXL - 21:9 landscape 1536x640":
            width, height = 1536, 640                
        
        width, height = height, width
        
        latent = torch.zeros([batch_size, 4, height // 8, width // 8])

        return(width, height, {"samples":latent}, batch_size,)    

NODE_CLASS_MAPPINGS = {
    "AspectRatio": AspectRatio
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "AspectRatio": "Aspect Ratio"
}
