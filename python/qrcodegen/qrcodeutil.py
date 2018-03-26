#inject method to qrcode
import qrcodegen

def make_image(self, image_factory=None, box_size=10,  **kwargs):
    """
    Make an image from the QR Code data.

    If the data has not been compiled yet, make it first.
    """
    
    if image_factory is not None:
        assert issubclass(image_factory, BaseImage)
    else:
        # Use PIL by default
        from qrcodegen.image.pil import PilImage
        image_factory = PilImage

    im = image_factory(
        4, self._size, box_size, **kwargs)
    for r in range(self._size):
        for c in range(self._size):
            if self._modules[r][c]:
                im.drawrect(r, c)
    return im

qrcodegen.QrCode.make_image = make_image