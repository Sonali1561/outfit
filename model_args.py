from dataclasses import dataclass

@ dataclass
class Args:
    data_dir = 'C:/Users/owj04/Desktop/polyvore_outfits'
    checkpoint_dir = 'F:/Projects/OutfitTransformer/checkpoints'
    model_path = None
    
    # Dataset & Input Processor Settings
    polyvore_split = 'nondisjoint'
    categories = ['<bottoms>', '<outerwear>', '<tops>', '<scarves>', '<hats>', '<all-body>', '<accessories>', '<sunglasses>', '<shoes>', '<jewellery>', '<bags>']
    outfit_max_length = 16
    use_image = True
    use_text = True
    use_category = False
    text_max_length = 64

    # Embedder&Recommender Model Settings
    use_clip_embedding = False
    clip_huggingface = 'patrickjohncyh/fashion-clip'
    huggingface = 'sentence-transformers/all-MiniLM-L12-v2'
    hidden = 128
    n_layers = 6
    n_heads = 16

    @property
    def load_model(self):
        return True if self.model_path is not None else False