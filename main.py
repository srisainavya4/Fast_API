from datetime import datetime
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from database import SessionLocal
import models

app = FastAPI()
db = SessionLocal()

class OurBaseModel(BaseModel):
    class Config:
        orm_mode=True
        
class Invoice(OurBaseModel):
    id: int
    number: str
    amount: float
    instatus: str
    date: datetime
    

@app.get('/getbyid/{invoice_id}', response_model=Invoice, status_code=status.HTTP_200_OK)
def get_Single_Invoice(invoice_id:int):
    get_Single_Invoice=db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()
    if get_Single_Invoice is not None:
        return get_Single_Invoice
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invoice not found")
    
@app.post('/addinvoice', response_model=Invoice, status_code=status.HTTP_201_CREATED)
def add_Invoice(invoice:Invoice):
    newInvoice=models.Invoice(
        id= invoice.id,
        number= invoice.number,
        amount= invoice.amount,
        instatus= invoice.instatus,
        date= invoice.date
    )   
    find_invoice =db.query(models.Invoice).filter(models.Invoice.id == invoice.id).first()
    if find_invoice is not None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Invoice with this id already exist")
    
    db.add(newInvoice)
    db.commit()
    return newInvoice

@app.put('/update_invoice/{invoice_id}', response_model=Invoice, status_code=status.HTTP_202_ACCEPTED)
def updateInvoice(invoice_id: int, invoice:Invoice):
    find_invoice = db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()
    if find_invoice is not None:
        find_invoice.id = invoice.id
        find_invoice.number = invoice.number
        find_invoice.amount = invoice.amount
        find_invoice.instatus = invoice.instatus
        find_invoice.date = invoice.date
        db.commit()
        return find_invoice
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invoice with this id not found")
  
@app.delete("/delete_invoice/{invoice_id}", response_model=Invoice, status_code=200)
def deleteInvoice(invoice_id:int):
    find_invoice = db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()
    if find_invoice is not None:
        db.delete(find_invoice)
        db.commit()
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Invoice deleted Successfully")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invoice with this id is either deleted or not found")
  