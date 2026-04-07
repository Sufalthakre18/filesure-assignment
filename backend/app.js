import express from "express";
import cors from "cors";
import connectDB from "./db.js";
import companiesRouter from "./routes/companies.js";

const app = express();

app.use(cors());
app.use(express.json());

connectDB();

app.use("/companies", companiesRouter);
app.get("/",(_,res)=>{
    res.send('api is running');
})

app.listen(5000, () => {
  console.log("🚀 Server running on port 5000");
});