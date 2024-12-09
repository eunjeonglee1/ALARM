import bs4
from langchain.document_loaders import WebBaseLoader

def webload(site):
    loader = WebBaseLoader(
        web_paths=(site,),
        bs_kwargs=dict(
            parse_only=bs4.SoupStrainer(
                class_=("view2_summary_in", "ready_ingre3", "view_step"),
                id=('recipeIntro', 'divConfirmedMaterialArea', 'obx_recipe_step_start',)
            )
        ),
    )
    site_document = loader.load()
    return site_document