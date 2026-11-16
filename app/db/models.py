from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db.session import Base

class ScanRecord(Base):
    __tablename__ = "scan_records"

    id = Column(Integer, primary_key=True, index=True)
    target_asset = Column(String, index=True, nullable=False)
    scanner_name = Column(String, default="trivy")
    scan_timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    total_vulnerabilities = Column(Integer, default=0)
    critical_count = Column(Integer, default=0)
    high_count = Column(Integer, default=0)

    findings = relationship("VulnerabilityFinding", back_populates="scan", cascade="all, delete-orphan")

class VulnerabilityFinding(Base):
    __tablename__ = "vulnerability_findings"

    id = Column(Integer, primary_key=True, index=True)
    scan_id = Column(Integer, ForeignKey("scan_records.id"), nullable=False)
    cve_id = Column(String, index=True, nullable=False)
    package_name = Column(String, nullable=False)
    installed_version = Column(String, nullable=False)
    fixed_version = Column(String, nullable=True)
    severity = Column(String, index=True, nullable=False)
    cvss_score = Column(Float, default=0.0)
    is_remediated = Column(Boolean, default=False)

    scan = relationship("ScanRecord", back_populates="findings")
