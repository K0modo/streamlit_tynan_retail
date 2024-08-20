from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    backref
    )



class Base(DeclarativeBase):
    pass

class BusinessLine(Base):
    __tablename__ = 'business_line'

    line_id: Mapped[str] = mapped_column(String(2), primary_key=True, nullable=False)
    line_name: Mapped[str] = mapped_column(String(15), nullable=False)

    # categories = relationship("ProductCategory", backref=backref("business_line"), cascade="all, delete-orphan")

    def __repr__(self):
        return f"BusinessLine: line_id= {self.line_id}, line_name= {self.line_name} "


class ProductCategory(Base):
    __tablename__ = 'product_category'

    prod_cat: Mapped[str] = mapped_column(String(6), primary_key=True, nullable=False)
    cat_name: Mapped[str] = mapped_column(String(25), nullable=False)
    line_id: Mapped[str] = mapped_column(ForeignKey(BusinessLine.line_id), nullable=True)

    def __repr__(self):
        return f"ProductCategory : prod_cat= {self.prod_cat}, cat_name= {self.cat_name},  line_id= {self.line_id} "


class ProductInventory(Base):
    __tablename__ = 'product_inventory'

    prod_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    prod_name: Mapped[str] = mapped_column(String(40), nullable=False)
    prod_desc: Mapped[str] = mapped_column(String(100), nullable=False)
    prod_width: Mapped[int] = mapped_column(nullable=True)
    prod_height: Mapped[int] = mapped_column(nullable=True)
    prod_depth: Mapped[int] = mapped_column(nullable=True)
    prod_price: Mapped[int] = mapped_column(nullable=False)
    prod_photo: Mapped[str] = mapped_column(nullable=True)
    line_id = mapped_column(ForeignKey(BusinessLine.line_id), nullable=True)
    prod_cat = mapped_column(ForeignKey(ProductCategory.prod_cat), nullable=True)

    def __repr__(self):
        return f"Product Inventory: prod_id={self.prod_id}, prod_name={self.prod_name}, prod_desc={self.prod_desc}, " \
               f"prod_price={self.prod_price}, prod_photo={self.prod_photo}, line_id={self.line_id}, " \
               f"prod_cat={self.prod_cat}, prod_width= {self.prod_width}, prod_height= {self.prod_height}, prod_depth={self.prod_depth}"


# class ProductDimensions(Base):
#     __tablename__ = 'product_dimensions'
#
#     prod_id: Mapped[int] = mapped_column(ForeignKey(ProductInventory.prod_id), nullable=False)
#     prod_width: Mapped[int]
#     prod_height: Mapped[int]
#     prod_depth: Mapped[int]
#
    # def __repr__(self):
    #     return f"ProductCategory : prod_id= {self.prod_id}, prod_width= {self.prod_width}," \
    #            f"  prod_height= {self.prod_height}, prod_depth={self.prod_depth} "

