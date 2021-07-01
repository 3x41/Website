<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl = "http://www.w3.org/1999/XSL/Transform">
	
	<xsl:template match = "/yey">
	
	
	<html>
		<body>
			<h2>Computers</h2>
			
			<xsl:for-each select="computers">
			
				<xsl:value-of select="namee" /><br />
			<xsl:value-of select="year" /><br />
			<xsl:value-of select="info" /><br />
			
			</xsl:for-each>
			
			
		
		</body>
		
	</html>
	
	
	
	</xsl:template>
	
	
	
</xsl:stylesheet>
	
