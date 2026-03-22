from pypdf import PdfReader, PdfWriter, Transformation

bg = PdfReader("page.pdf")        # your border page
nb = PdfReader("subrat.pdf")        # notebook export
writer = PdfWriter()

scale = 0.8

for i in range(len(nb.pages)):
    template_page = bg.pages[0]
    notebook_page = nb.pages[i]

    # Get sizes
    tw = float(template_page.mediabox.width)
    th = float(template_page.mediabox.height)

    nw = float(notebook_page.mediabox.width)
    nh = float(notebook_page.mediabox.height)

    # Scale + center
    tx = (tw - nw * scale) / 2
    ty = (th - nh * scale) / 2

    transformation = Transformation().scale(scale).translate(tx, ty)

    notebook_page.add_transformation(transformation)

    # Merge
    template_page.merge_page(notebook_page)
    writer.add_page(template_page)

with open("subrattt.pdf", "wb") as f:
    writer.write(f)