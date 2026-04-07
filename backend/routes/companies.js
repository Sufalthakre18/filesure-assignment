import express from "express";
import mongoose from "mongoose";

const router = express.Router();

const Company = mongoose.model(
  "Company",
  new mongoose.Schema({}, { strict: false })
);

// GET companies
router.get("/", async (req, res) => {
  try {
    const { page = 1, limit = 10, status, state } = req.query;

    const query = {};
    if (status) query.status = status;
    if (state) query.state = state;

    const data = await Company.find(query)
      .skip((page - 1) * limit)
      .limit(parseInt(limit));

    const total = await Company.countDocuments(query);

    res.json({
      data,
      page: Number(page),
      total
    });

  } catch (err) {
    res.status(500).json({ error: "Server error" });
  }
});

// summary
router.get("/summary", async (req, res) => {
  try {
    const summary = await Company.aggregate([
      { $group: { _id: "$status", count: { $sum: 1 } } }
    ]);

    res.json(summary);
  } catch (err) {
    res.status(500).json({ error: "Summary error" });
  }
});

export default router;